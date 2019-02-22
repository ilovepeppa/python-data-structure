import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len - 5)


def tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(t, branch_len - 15)
        t.left(40)
        tree(t, branch_len - 15)
        t.right(20)
        t.backward(branch_len)


def draw_triangle(t, points, color):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(t, points, degree):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(t, points, colormap[degree])

    if degree > 0:
        sierpinski(t, [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1)
        sierpinski(t, [get_mid(points[0], points[1]), points[1], get_mid(points[1], points[2])], degree - 1)
        sierpinski(t, [get_mid(points[0], points[2]), get_mid(points[1], points[2]), points[2]], degree - 1)


my_points = [[-100, -50], [0, 100], [100, -50]]
sierpinski(my_turtle, my_points, 4)
my_win.exitonclick()
