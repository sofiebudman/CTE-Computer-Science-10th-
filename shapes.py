import turtle
def oval(rad):
    for i in range (2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)

def rect(x,y,turn):
    for i in range(2):
        turtle.forward(x)
        turtle.right(turn)
        turtle.forward(y)
        turtle.right(turn)

def curve(isRight,scope,degree,step):
    for i in range (scope):
        if (isRight):
            turtle.right(degree)
        else:
            turtle.left(degree)
        turtle.forward(step)
def line(angle,length):
    turtle.seth(angle)
    turtle.fd(length)

#hammer
def drawHammer():
    turtle.width(3)
    turtle.pencolor('orange')
    turtle.seth(-10)
    curve(False,5,6,3)
    line(100,50)
    line(10,30)
    turtle.left(60)
    curve(False,20,3,2)
    line(10,-30)
    turtle.seth(90)
    turtle.circle(5,200)
    line(10,10)
    line(10,-40)
    turtle.right(130)
    curve(False,20,3,2)
    turtle.left(70)
    turtle.forward(50)
    turtle.fd(-20)
    turtle.right(90)
    turtle.fd(50)
def drawPlane():
    turtle.width(3)
    turtle.pencolor('orange')
    line(50,20)
    turtle.right(70)
    turtle.forward(25)
    turtle.left(110)
    turtle.forward(70)
    turtle.left(160)
    turtle.forward(65)

    turtle.right(20)
    turtle.forward(20)
    turtle.right(130)
    turtle.forward(20)
    turtle.right(43)
    turtle.forward(70)
    turtle.left(160)
    turtle.forward(75)
    turtle.left(110)
    turtle.forward(26)

def tag():
    turtle.width(3)
    turtle.pencolor('orange')
    turtle.seth(45)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(35)
    turtle.left(100)
    turtle.forward(35)
    turtle.left(40)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(45)
    turtle.penup()
    turtle.fd(-11)
    turtle.left(90)
    turtle.fd(15)
    turtle.pd()
    turtle.forward(45)
    turtle.pu()
    turtle.left(90)
    turtle.forward(11)
    turtle.pd()
    turtle.left(90)
    turtle.forward(45)
    turtle.pu()
    turtle.right(90)
    turtle.forward(11)
    turtle.right(90)
    turtle.pd()
    turtle.fd(45)
    turtle.pu()
    turtle.forward(24)
    turtle.right(90)
    turtle.forward(12)
    turtle.pd()
    turtle.circle(3)
    turtle.pu()
    turtle.right(-90)
    turtle.forward(12)
    turtle.pd()
    turtle.right(140)
    turtle.circle(7,180)
    turtle.circle(-7,180)
    turtle.circle(7,180)
    input('hit enter')

tag()


