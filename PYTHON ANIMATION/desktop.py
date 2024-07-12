import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def on_button_click():
    user_input = entry.get()
    selected_option = radio_var.get()
    checked_options = [var.get() for var in checkbox_vars]
    selected_dropdown = dropdown_var.get()
    selected_listbox = listbox.curselection()

    selected_items = [listbox.get(i) for i in selected_listbox]

    info_message = (
        f"You entered: {user_input}\n"
        f"Selected option: {selected_option}\n"
        f"Checked options: {checked_options}\n"
        f"Selected from dropdown: {selected_dropdown}\n"
        f"Selected from listbox: {', '.join(selected_items)}"
    )
    messagebox.showinfo("Information", info_message)

# Create the main window
root = tk.Tk()
root.title("Advanced GUI")

# Create and organize frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

option_frame = tk.Frame(root)
option_frame.pack(pady=10)

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

dropdown_frame = tk.Frame(root)
dropdown_frame.pack(pady=10)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create a label and entry
label = tk.Label(input_frame, text="Enter something:")
label.grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(input_frame, width=40)
entry.grid(row=0, column=1, padx=10, pady=5)

# Create radio buttons
radio_var = tk.StringVar(value="Option 1")
tk.Label(option_frame, text="Choose an option:").pack(anchor='w')
radio1 = tk.Radiobutton(option_frame, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(option_frame, text="Option 2", variable=radio_var, value="Option 2")
radio3 = tk.Radiobutton(option_frame, text="Option 3", variable=radio_var, value="Option 3")
radio1.pack(anchor='w')
radio2.pack(anchor='w')
radio3.pack(anchor='w')

# Create checkboxes
checkbox_vars = [tk.StringVar(value="Unchecked") for _ in range(3)]
tk.Label(checkbox_frame, text="Check some options:").pack(anchor='w')
checkbox1 = tk.Checkbutton(checkbox_frame, text="Check 1", variable=checkbox_vars[0], onvalue="Checked 1", offvalue="Unchecked")
checkbox2 = tk.Checkbutton(checkbox_frame, text="Check 2", variable=checkbox_vars[1], onvalue="Checked 2", offvalue="Unchecked")
checkbox3 = tk.Checkbutton(checkbox_frame, text="Check 3", variable=checkbox_vars[2], onvalue="Checked 3", offvalue="Unchecked")
checkbox1.pack(anchor='w')
checkbox2.pack(anchor='w')
checkbox3.pack(anchor='w')

# Create a dropdown (combobox)
dropdown_var = tk.StringVar(value="Option A")
tk.Label(dropdown_frame, text="Select from dropdown:").pack(anchor='w')
dropdown = ttk.Combobox(dropdown_frame, textvariable=dropdown_var)
dropdown['values'] = ("Option A", "Option B", "Option C")
dropdown.pack(pady=5)

# Create a listbox
tk.Label(listbox_frame, text="Select items from listbox:").pack(anchor='w')
listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE)
listbox.pack()
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)

# Create a button
button = tk.Button(button_frame, text="Submit", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
