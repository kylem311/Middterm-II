import turtle

########### Your Code here ##############
import math


	
def drawSineCurve(dart):
	'''
	draws sign curve
	args: none
	Return: sign curve
	'''
	for i in range(-360,361):
		dart.down()
		dart.goto(i, math.sin(math.radians(i)))
		dart.up()
	dart.goto(0,0)

def drawCosineCurve(dart):
	'''
	draws cosine curve
	args: none
	Return: cosign curve
	'''
	dart.up()
	dart.goto(-360,1)
	
	for i in range(-360,361):
		dart.down()
		dart.goto(i, math.cos(math.radians(i)))
	dart.up()	
	dart.goto(0,0)

def drawTangentCurve(dart):
	'''
	draws tangent curve
	args: none
	Return: tangent curve
	'''
	dart.goto(0,0)
	for i in range(-360,361):
		dart.down()
		dart.goto(i, math.tan(math.radians(i)))
		dart.up()
	dart.goto(0,0)

def drawNaturalLog(dart):
	'''
	draws natural log graph
	args: i cant equal 0
	Return: natural log graph
	'''
	for i in range(-360,361):
		if i > 0:
			dart.down()
			dart.goto(i, math.log(math.radians(i)))
   		

def setupWindow(wn):
	'''
	creates the window, sets perameters , and sets background to light blue
	args: none
	Return: light blue window
	'''
	wn = turtle.Screen()
	wn.setworldcoordinates(-360,-1,360,1)
	wn.bgcolor('lightblue')
	
	

def setupAxis(dart):
	'''
	draws a x and y axis
	args: none
	Return: x and y axis
	'''

	dart = turtle.Turtle()
	dart.speed(9)
	for i in [0,360,0,-360]:
		dart.goto(i,0)
	for i in [0,1,0,-1,0]:
		dart.goto(0,i)
	
	
	






##########  Do Not Alter Any Code Past Here ########

def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    drawNaturalLog(dart)
    wn.exitonclick()


main()


