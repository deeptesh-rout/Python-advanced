import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rainbow Circle Spiral")

# Set up the turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Set the turtle speed to the maximum

# Function to draw the circular rainbow pattern
def draw_rainbow_circle():
    num_circles = 80
    num_steps = 80
    hue = 0  # Start with red color
    radius_increment = 5  # Increment radius for each circle
    
    for j in range(num_circles):
        spiral_turtle.penup()
        spiral_turtle.goto(0, -radius_increment * j)  # Move the turtle to the starting position
        spiral_turtle.pendown()
        
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        spiral_turtle.pencolor(color)
        
        spiral_turtle.circle(radius_increment * j)  # Draw a circle with increasing radius
        
        hue += 1 / num_circles  # Increment the hue to get a rainbow effect

# Draw the circular rainbow pattern
draw_rainbow_circle()

# Hide the turtle
spiral_turtle.hideturtle()

# Keep the window open until clicked
screen.mainloop()
