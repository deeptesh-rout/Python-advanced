import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Growing Starburst")

# Set up the turtle
star_turtle = turtle.Turtle()
star_turtle.speed(0)  # Set the turtle speed to the maximum

# Function to draw the growing starburst
def draw_growing_starburst():
    num_lines = 36  # Number of lines for the starburst
    angle = 360 / num_lines
    hue = 0  # Start with red color
    length = 10  # Initial length of the line
    for i in range(num_lines):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        star_turtle.pencolor(color)
        for _ in range(5):  # Draw a small line
            star_turtle.forward(length)
            star_turtle.backward(length)
            star_turtle.left(10)
        star_turtle.right(angle)
        hue += 1 / num_lines  # Increment the hue to get a color change
        length += 5  # Increase the length of the line

# Draw the growing starburst
draw_growing_starburst()

# Hide the turtle
star_turtle.hideturtle()

# Keep the window open until clicked
screen.mainloop()
