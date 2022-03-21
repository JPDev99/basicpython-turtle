import turtle
tao = turtle.Pen()
tao.shape('turtle')


def Wong():
    for i in range(15):
        tao.circle(50)
        tao.left(24)


def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()




def Wonwong():
    r = 10
    for i in range(100):
        tao.circle(r + i,45)
