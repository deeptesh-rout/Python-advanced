from datetime import datetime, timedelta

class Appointment:
    def __init__(self, title, startTime, endTime):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
    
    def __str__(self):
        return f"Title: {self.title}, Start Time: {self.startTime.strftime('%Y-%m-%d %H:%M')}, End Time: {self.endTime.strftime('%Y-%m-%d %H:%M')}"

    def __eq__(self, other):
        return isinstance(other, Appointment) and self.title == other.title and self.startTime == other.startTime and self.endTime == other.endTime
    
    def __hash__(self):
        return hash((self.title, self.startTime, self.endTime))

class Scheduler:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        for a in self.appointments:
            if appointment.startTime < a.endTime and appointment.endTime > a.startTime:
                return False  # Conflict detected
        self.appointments.append(appointment)
        return True

    def remove_appointment(self, appointment):
        self.appointments = [a for a in self.appointments if a != appointment]
        return True

    def get_appointments(self, startDate, endDate):
        return [a for a in self.appointments if a.startTime <= endDate and a.endTime >= startDate]

    def edit_appointment(self, oldAppointment, newAppointment):
        if self.remove_appointment(oldAppointment):
            if self.add_appointment(newAppointment):
                return True
            else:
                # If adding the new appointment fails, re-add the old appointment
                self.add_appointment(oldAppointment)
        return False

    def is_available(self, startTime, endTime):
        for a in self.appointments:
            if startTime < a.endTime and endTime > a.startTime:
                return False
        return True

    def find_next_available_slot(self, startTime, durationMinutes):
        potentialStart = startTime
        potentialEnd = startTime + timedelta(minutes=durationMinutes)

        while True:
            if self.is_available(potentialStart, potentialEnd):
                return potentialStart
            potentialStart += timedelta(minutes=1)

    def count_appointments(self, startDate, endDate):
        return len(self.get_appointments(startDate, endDate))

    def cancel_all_appointments_for_day(self, date):
        self.appointments = [a for a in self.appointments if not (a.startTime.date() == date.date())]

    def get_appointment_summary_by_day(self, startDate, endDate):
        summary = {}
        currentDate = startDate
        while currentDate <= endDate:
            startOfDay = currentDate.replace(hour=0, minute=0, second=0)
            endOfDay = currentDate.replace(hour=23, minute=59, second=59)
            count = len(self.get_appointments(startOfDay, endOfDay))
            summary[currentDate.strftime('%Y-%m-%d')] = count
            currentDate += timedelta(days=1)
        return summary

    def find_longest_free_slot(self, startDate, endDate):
        sortedAppointments = sorted(self.get_appointments(startDate, endDate), key=lambda a: a.startTime)

        longestFreeSlot = None
        maxDuration = timedelta(0)
        previousEnd = startDate

        for appointment in sortedAppointments:
            currentStart = appointment.startTime
            if previousEnd < currentStart:
                freeSlotDuration = currentStart - previousEnd
                if freeSlotDuration > maxDuration:
                    maxDuration = freeSlotDuration
                    longestFreeSlot = (previousEnd, currentStart)
            previousEnd = appointment.endTime

        if previousEnd < endDate:
            freeSlotDuration = endDate - previousEnd
            if freeSlotDuration > maxDuration:
                longestFreeSlot = (previousEnd, endDate)

        return longestFreeSlot

    def get_all_appointments(self):
        return self.appointments[:]

def main():
    scheduler = Scheduler()

    # Add some sample appointments
    scheduler.add_appointment(Appointment("Meeting", datetime(2024, 3, 1, 10, 0, 0), datetime(2024, 3, 1, 11, 0, 0)))
    scheduler.add_appointment(Appointment("Lunch", datetime(2024, 3, 1, 12, 0, 0), datetime(2024, 3, 1, 13, 0, 0)))
    scheduler.add_appointment(Appointment("Presentation", datetime(2024, 3, 1, 14, 0, 0), datetime(2024, 3, 1, 15, 0, 0)))
    scheduler.add_appointment(Appointment("Review", datetime(2024, 3, 1, 16, 0, 0), datetime(2024, 3, 1, 17, 0, 0)))
    scheduler.add_appointment(Appointment("Workshop", datetime(2024, 3, 1, 17, 30, 0), datetime(2024, 3, 1, 18, 30, 0)))

    # Get appointments for a specific date range (user input)
    startDate = read_date_time("Enter start date and time (yyyy-MM-dd HH:mm): ")
    endDate = read_date_time("Enter end date and time (yyyy-MM-dd HH:mm): ")
    appointments = scheduler.get_appointments(startDate, endDate)

    # Print the appointments
    print(f"Appointments for {startDate} to {endDate}:")
    for appointment in appointments:
        print(appointment)

    # Edit an appointment (user input)
    oldAppointment = Appointment("Lunch", datetime(2024, 3, 1, 12, 0, 0), datetime(2024, 3, 1, 13, 0, 0))
    print("Enter details for the new appointment:")
    title = input("Enter title: ")
    newStartTime = read_date_time("Enter new start time (yyyy-MM-dd HH:mm): ")
    newEndTime = read_date_time("Enter new end time (yyyy-MM-dd HH:mm): ")
    newAppointment = Appointment(title, newStartTime, newEndTime)

    if scheduler.edit_appointment(oldAppointment, newAppointment):
        print("Appointment edited successfully.")
    else:
        print("Failed to edit appointment due to conflict.")

    # Print the updated appointments
    appointments = scheduler.get_appointments(startDate, endDate)
    print(f"Updated appointments for {startDate} to {endDate}:")
    for appointment in appointments:
        print(appointment)

    # Check availability for a specific time slot (user input)
    checkStartTime = read_date_time("Enter start time to check availability (yyyy-MM-dd HH:mm): ")
    checkEndTime = read_date_time("Enter end time to check availability (yyyy-MM-dd HH:mm): ")
    if scheduler.is_available(checkStartTime, checkEndTime):
        print(f"The time slot from {checkStartTime} to {checkEndTime} is available.")
    else:
        print(f"The time slot from {checkStartTime} to {checkEndTime} is not available.")

    # Find the next available time slot of 60 minutes (user input)
    nextAvailableSlotStart = read_date_time("Enter start time to find next available slot (yyyy-MM-dd HH:mm): ")
    durationMinutes = read_integer("Enter duration of the slot in minutes: ")
    nextAvailableSlot = scheduler.find_next_available_slot(nextAvailableSlotStart, durationMinutes)
    if nextAvailableSlot:
        print(f"The next available time slot is at {nextAvailableSlot}.")
    else:
        print("No available time slot found.")

    # Count the number of appointments on a specific date (user input)
    countAppointmentsDate = read_date_time("Enter date to count appointments (yyyy-MM-dd): ")
    appointmentCount = scheduler.count_appointments(countAppointmentsDate, countAppointmentsDate + timedelta(days=1) - timedelta(seconds=1))
    print(f"Number of appointments on {countAppointmentsDate.date()}: {appointmentCount}")

    # Cancel all appointments for a specific day (user input)
    cancelAppointmentsDate = read_date_time("Enter date to cancel all appointments (yyyy-MM-dd): ")
    scheduler.cancel_all_appointments_for_day(cancelAppointmentsDate)
    print(f"All appointments for {cancelAppointmentsDate.date()} have been canceled.")

    # Get a summary of appointments by day (user input)
    summaryStartDate = read_date_time("Enter start date to get appointment summary (yyyy-MM-dd): ")
    summaryEndDate = read_date_time("Enter end date to get appointment summary (yyyy-MM-dd): ")
    summary = scheduler.get_appointment_summary_by_day(summaryStartDate, summaryEndDate)
    print("Appointment summary by day:")
    for date, count in summary.items():
        print(f"{date}: {count} appointments")

    # Find the longest free slot available (user input)
    longestFreeSlotStartDate = read_date_time("Enter start date to find longest free slot (yyyy-MM-dd HH:mm): ")
    longestFreeSlotEndDate = read_date_time("Enter end date to find longest free slot (yyyy-MM-dd HH:mm): ")
    longestFreeSlot = scheduler.find_longest_free_slot(longestFreeSlotStartDate, longestFreeSlotEndDate)
    if longestFreeSlot:
        print(f"The longest free slot is from {longestFreeSlot[0]} to {longestFreeSlot[1]}.")
    else:
        print("No free slot found.")

    # Get all appointments
    allAppointments = scheduler.get_all_appointments()
    print("All appointments:")
    for appointment in allAppointments:
        print(appointment)

    # Keep the console window open in debug mode.
    input("Press any key to exit...")

# Helper method to read DateTime from user input
def read_date_time(message):
    while True:
        try:
            return datetime.strptime(input(message), "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date/time format. Please enter again.")

# Helper method to read integer from user input
def read_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
