import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rainbow Spiral")

# Set up the turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Set the turtle speed to the maximum

# Function to draw the spiral
def draw_rainbow_spiral():
    num_lines = 360
    hue = 0  # Start with red color
    for i in range(num_lines):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        spiral_turtle.pencolor(color)
        spiral_turtle.forward(i)
        spiral_turtle.left(59)
        hue += 1 / num_lines  # Increment the hue to get a rainbow effect

# Draw the rainbow spiral
draw_rainbow_spiral()

# Hide the turtle
spiral_turtle.hideturtle()

# Keep the window open until clicked
screen.mainloop()
