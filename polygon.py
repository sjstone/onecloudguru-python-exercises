import turtle

def do_polygon(size, number_of_sides):
    for i in range(number_of_sides):
        turtle.fd(size)
        turtle.lt(360/number_of_sides)


do_polygon(100, 2)
do_polygon(100, 4)
do_polygon(200, 3)
do_polygon(100, 8)