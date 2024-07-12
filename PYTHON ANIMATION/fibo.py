import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Set the speed to the fastest
turtle.delay(200)  # Set delay between turtle movements (in milliseconds)

# Function to generate Fibonacci numbers
def fibonacci(n):
    fib_series = [0, 1]  # Initialize with the first two Fibonacci numbers
    
    # Generate Fibonacci sequence up to the nth term
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series

# Define the number of Fibonacci terms
num_terms = 15

# Draw the Fibonacci spiral with advanced features
fib_series = fibonacci(num_terms)
for i in range(num_terms):
    # Change color using a gradient
    hue = float(i) / num_terms
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    spiral.color(color)
    
    # Draw the segment proportional to the Fibonacci number
    for _ in range(2):  # Insert additional lines to slow down the drawing
        spiral.forward(fib_series[i] * 5 / 2)  # Divide by a factor to insert more lines
        spiral.right(90)
    
    spiral.forward(fib_series[i] * 5 / 2)  # Draw the final portion of the segment
    spiral.right(90)  # Rotate the turtle by 90 degrees

# Hide the turtle and display the final spiral
spiral.hideturtle()

# Close the window when clicked
screen.exitonclick()
