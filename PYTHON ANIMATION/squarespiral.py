import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rainbow Square Spiral")

# Set up the turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Set the turtle speed to the maximum

# Function to draw the square spiral
def draw_rainbow_square_spiral():
    num_lines = 360
    hue = 0  # Start with red color
    for i in range(num_lines):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        spiral_turtle.pencolor(color)
        spiral_turtle.forward(i * 2)  # Increase the forward movement to create a square spiral
        spiral_turtle.right(90)  # Turn right by 90 degrees to form square angles
        hue += 1 / num_lines  # Increment the hue to get a rainbow effect

# Draw the rainbow square spiral
draw_rainbow_square_spiral()

# Hide the turtle
spiral_turtle.hideturtle()

# Keep the window open until clicked
screen.mainloop()
