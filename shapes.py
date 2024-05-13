import turtle

def oval(bigR,smallR):
    turtle.circle(bigR,90)
    turtle.circle(smallR,90)
    turtle.circle(bigR,90)
    turtle.circle(smallR,90)
   

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

#map
def drawMap():
    turtle.width(3)
    turtle.penup()
    turtle.pencolor('orange')
    turtle.goto(-450,300)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(70)
    turtle.right(45)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(45)
    turtle.forward(70)
    turtle.right(135)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.left(45)
    turtle.forward(70)
    for i in range(3):
        turtle.right(135)
        turtle.forward(15)
        turtle.right(45)
        turtle.forward(70)
        turtle.left(135)
        turtle.forward(15)
        turtle.left(45)
        turtle.forward(70)
#hammer()
def drawHammer():
    turtle.pu()
    turtle.goto(-300,300)
    turtle.seth(0)
    turtle.pd()
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
    turtle.pu()
    turtle.goto(-230,300)
    turtle.pd()
    turtle.seth(0)
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
def drawTag():
    turtle.pu()
    turtle.goto(-150,300)
    turtle.pd()
    turtle.seth(0)
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
def drawBread():
    turtle.pencolor('orange')
    turtle.width(3)
    turtle.pu()
    turtle.goto(-30,300)
    turtle.pd()
    turtle.seth(10)
    oval(50,14)
    turtle.pu()
    turtle.seth(80)
    turtle.fd(60)
    turtle.right(40)
    turtle.fd(10)
    turtle.pd()
    turtle.seth(310)
    turtle.forward(25)
    turtle.pu()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(110)
    turtle.pd()
    curve(False,3,10,10)
    turtle.pu()
    turtle.left(90)
    turtle.forward(7)
    turtle.left(90)
    turtle.pd()
    curve(True,3,10,10)
    turtle.pu()
    turtle.right(90)
    turtle.forward(7)
    turtle.left(90)
    turtle.fd(5)
    turtle.right(180)
    turtle.pd()
    curve(False,3,10,10)
    turtle.pu()
    turtle.left(90)
    turtle.fd(10)
    turtle.left(95)
    turtle.pd()
    curve(True,3,10,10)
    turtle.pu()
    turtle.right(90)
    turtle.fd(7)
    turtle.right(90)
    turtle.pd()
    curve(False,3,10,7)
    turtle.pu()
    turtle.goto(-27,309)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.right(90)
    turtle.fd(7)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.right(110)
    turtle.fd(6)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.seth(45)
    turtle.forward(10)
    turtle.dot(3)
    turtle.pu()
    turtle.fd(10)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.right(-10)
    turtle.fd(7)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.forward(6)
    turtle.pd()
    turtle.dot(3)
def drawBandaid():
    turtle.pu()
    turtle.width(3)
    turtle.pencolor('orange')
    turtle.goto(20,320)
    turtle.pd()
    turtle.seth(225)
    turtle.circle(18,180)
    turtle.forward(80)
    turtle.circle(18,180)
    turtle.forward(80)
    turtle.forward(-15)
    turtle.left(90)
    turtle.forward(36)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(36)
    turtle.pu()
    turtle.fd(-6)
    turtle.right(90)
    turtle.forward(6)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)
    turtle.pu()
    turtle.right(90)
    turtle.fd(8)
    turtle.right(90)
    turtle.fd(5)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)
    turtle.pu()
    turtle.left(90)
    turtle.fd(8)
    turtle.left(90)
    turtle.fd(5)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)

    turtle.pu()
    turtle.right(90)
    turtle.fd(8)
    turtle.right(90)
    turtle.fd(5)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)

    turtle.pu()
    turtle.forward(60)

    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)
    turtle.pu()
    turtle.left(90)
    turtle.fd(-8)
    turtle.left(90)
    turtle.fd(5)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)
    turtle.pu()
    turtle.right(90)
    turtle.fd(-8)
    turtle.right(90)
    turtle.fd(5)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)

    turtle.pu()
    turtle.left(90)
    turtle.fd(-8)
    turtle.left(90)
    turtle.fd(5)
    for i in range(4):
        turtle.pd()
        turtle.dot(3)
        turtle.pu()
        turtle.fd(5)
def drawPuzzle():
    turtle.pu()
    turtle.width(3)
    turtle.pencolor('orange')
    turtle.goto(170,300)
    turtle.pd()
    turtle.seth(135)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(110)
    turtle.circle(-15,220)
    turtle.left(110)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(110)
    turtle.circle(10,220)
    turtle.right(110)
    turtle.forward(28)
    turtle.right(90)
    turtle.forward(10)

def drawWrench():
    turtle.pu()
    turtle.pencolor('green')
    turtle.width(3)
    turtle.goto(-390,200)
    turtle.seth(110)
    turtle.pd()
    turtle.circle(-30,140)
    turtle.right(115)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(18)
    turtle.left(60)
    turtle.forward(18)
    turtle.left(60)
    turtle.forward(30)
    turtle.right(110)
    turtle.circle(-30,140)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(70)

    turtle.circle(-30,140)
    turtle.right(115)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(18)
    turtle.left(60)
    turtle.forward(18)
    turtle.left(60)
    turtle.forward(30)
    turtle.right(110)
    turtle.circle(-30,140)

    turtle.left(73)
    turtle.forward(75)
def drawMagnet():
    turtle.pu()
    turtle.width(3)
    turtle.pencolor('green')
    turtle.goto(-300,200)
    turtle.seth(110)
    turtle.pd()
    turtle.forward(20)
    curve(True,70,3,2)
    turtle.right(5)
    turtle.forward(20)
    turtle.right(80)
    turtle.forward(12)
    turtle.right(100)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(12)
    turtle.fd(-12)
    turtle.left(90)
    curve(False,73,3,1.3)
    turtle.right(90)
    turtle.forward(12)
    turtle.fd(-12)
    turtle.left(80)
    turtle.fd(20)
    turtle.right(100)
    turtle.fd(12)
    turtle.pu()
    turtle.goto(-303,195)
    turtle.seth(230)
    turtle.pd()
    turtle.forward(7)
    turtle.pu()
    turtle.goto(-298,195)
    turtle.seth(260)
    turtle.pd()
    turtle.forward(7)
    turtle.pu()
    turtle.goto(-290,194)
    turtle.seth(265)
    turtle.pd()
    turtle.forward(7)
    turtle.pu()
    turtle.goto(-250,195)
    turtle.seth(250)
    turtle.pd()
    turtle.forward(7)
    turtle.pu()
    turtle.goto(-244,195)
    turtle.seth(275)
    turtle.pd()
    turtle.fd(7)
    turtle.pu()
    turtle.goto(-237,196)
    turtle.seth(290)
    turtle.pd()
    turtle.fd(7)
def drawScrew():
    turtle.pu()
    turtle.width(3)
    turtle.pencolor('green')
    turtle.goto(-210,200)
    turtle.seth(60)
    turtle.pd()
    turtle.forward(18)
    turtle.left(50)
    turtle.forward(5)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(18)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(18)
    turtle.fd(-5)
    turtle.seth(60)
    turtle.pu()
    turtle.fd(5)
    turtle.pd()
    turtle.fd(12)
    turtle.left(50)
    turtle.forward(5)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(18)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(18)
    turtle.fd(-5)
    turtle.seth(60)
    turtle.pu()
    turtle.fd(5)
    turtle.pd()
    turtle.fd(12)
    turtle.left(50)
    turtle.forward(5)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(18)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(18)
    turtle.fd(-5)
    turtle.seth(60)
    turtle.pu()
    turtle.fd(5)
    turtle.pd()
    turtle.fd(12)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.circle(-20,80)
    turtle.right(70)
    turtle.fd(14)
    turtle.left(160)
    turtle.fd(14)
    turtle.right(90)
    turtle.circle(-20,83)
    turtle.right(90)
    turtle.fd(30)
    turtle.fd(-14)
    turtle.seth(60)
    turtle.fd(-20)
    turtle.pu()
    turtle.fd(-6)
    turtle.pd()
    turtle.fd(-12)
    turtle.pu()
    turtle.fd(-6)
    turtle.pd()
    turtle.fd(-12)
    turtle.pu()
    turtle.fd(-6)
    turtle.right(180)
    turtle.right(30)
    turtle.pd()
    turtle.fd(18)
    
def drawPaintbrush():
    turtle.pu()
    turtle.pencolor('green')
    turtle.width(3)
    turtle.goto(-150,200)
    turtle.seth(190)
    turtle.pd()
    turtle.fd(20)
    turtle.circle(-6,90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(60)
    turtle.right(90)
    turtle.fd(20)
    turtle.circle(-6,90)
    turtle.fd(20)
    turtle.left(90)
    turtle.fd(10)
    turtle.circle(-5,180)
    turtle.fd(10)
    

#turtle.speed(10)
        
#drawMap()
#drawHammer()
#drawPlane()
#drawTag()
#drawBread()
#drawBandaid()
#drawPuzzle()
#drawWrench()
#drawMagnet()
#drawScrew()
drawPaintbrush()

#points: 12



