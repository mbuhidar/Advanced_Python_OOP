from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter canvas color (white or black): ')

# Create a canvas with the user data
canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

while True:
    shape_type = input("What shape would you like to draw? (Enter 'quit' to quit) ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter x position for rectange: '))
        rec_y = int(input('Enter y position for rectange: '))
        rec_width = int(input('Enter width for rectangle: '))
        rec_height = int(input('Enter height for rectangle: '))
        red = int(input('How much red should the rectangle have? '))
        green = int(input('How much green? '))
        blue = int(input('How much blue? '))
        
        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == 'square':
        sqr_x = int(input('Enter x position for square: '))
        sqr_y = int(input('Enter y position for square: '))
        sqr_side = int(input('Enter side length for square: '))
        red = int(input('How much red should the rectangle have? '))
        green = int(input('How much green? '))
        blue = int(input('How much blue? '))

        # Create the square
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    # Break the loop if user entered 'quit'
    if shape_type == 'quit':
        break

canvas.make('canvas.png')
