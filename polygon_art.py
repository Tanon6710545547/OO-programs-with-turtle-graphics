import turtle
import random

class PolygonDrawer:
    def __init__(self):
        turtle.speed(5)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def get_new_color(self):
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()

        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)

        turtle.penup()

    def draw_style(self, style):
        for _ in range(20):
            num_sides = random.randint(3, 5) if style in ['4', '8', '9'] else (
                3 if style in ['1', '5'] else (4 if style in ['2', '6'] else 5)
            )

            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 15)

            # draw a polygon at a random location, orientation, color, and border line thickness
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            if style in ['5', '6', '7', '8', '9']:
                reduction_ratio = 0.8
                repeat_count = 2 if style != '9' else random.randint(0, 2)

                for _ in range(repeat_count):
                    size *= reduction_ratio
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        return num_sides, size, orientation, location, color, border_size

    def embed_polygon(self, num_sides, size, orientation, location, color, border_size):
        # specify a reduction ratio to draw a smaller polygon inside the one above
        reduction_ratio = 0.618

        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.right(90)

        pos = turtle.pos()
        location[0], location[1] = pos[0], pos[1]

        # adjust the size according to the reduction ratio
        size *= reduction_ratio
        # draw the second polygon embedded inside the original 
        self.draw_polygon(num_sides, size, orientation, location, color, border_size)

    def run(self):
        style = input("function 1 - 9: ")
        num_sides, size, orientation, location, color, border_size = self.draw_style(style)
        self.embed_polygon(num_sides, size, orientation, location, color, border_size)
        turtle.done()


if __name__ == "__main__":
    drawer = PolygonDrawer()
    drawer.run()
