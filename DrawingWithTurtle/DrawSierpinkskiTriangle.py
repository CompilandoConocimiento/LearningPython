# ==========================================================================
# ==================     GRAPHING A SIERPINKSKI ============================
# ==========================================================================

import turtle                                                                           #How we draw it!
turtle.title("Sierpinski Triangle")                                                     #Name of the window
turtle.bgcolor("white")                                                                 #Color of the background

FractalDrawer = turtle.Turtle()                                                         #The object to draw    
FractalDrawer.ht()                                                                      #The thickness
FractalDrawer.speed(20)                                                                 #The speed when we draw a Fractal
FractalDrawer.pencolor('blue')                                                          #Find the color of the DrawTheTriangle

SetOfPoints = [[-280,-200],[0,280],[280,-200]]                                          #Size of DrawTheTriangle

def FindMiddlePoint(p1, p2):                                                            #Get the Center of 2 SetOfPoints
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)                                    #Find midpoint

def DrawTheTriangle(SetOfPoints, Depth):                                                #FUNCION: To create a new Triangle

    FractalDrawer.up()                                                                  #Move up
    FractalDrawer.goto(SetOfPoints[0][0], SetOfPoints[0][1])                            #Move where

    FractalDrawer.down()                                                                #Move up
    FractalDrawer.goto(SetOfPoints[1][0], SetOfPoints[1][1])                            #Move where
    FractalDrawer.goto(SetOfPoints[2][0], SetOfPoints[2][1])                            #Move where
    FractalDrawer.goto(SetOfPoints[0][0], SetOfPoints[0][1])                            #Move where

    if (Depth > 0) :                                                                    #If we still have work to do

        Depth = Depth -1                                                                #Remove one level of depthness

        DrawTheTriangle (
                [SetOfPoints[0],                                                        #Find we to start
                FindMiddlePoint(SetOfPoints[0], SetOfPoints[1]),                        #Find we to start
                FindMiddlePoint(SetOfPoints[0], SetOfPoints[2])],                       #Find we to start
                Depth)                                                                  #And the deep level

        DrawTheTriangle (
                [SetOfPoints[1],                                                        #Find we to start
                FindMiddlePoint(SetOfPoints[0], SetOfPoints[1]),                        #Find we to start
                FindMiddlePoint(SetOfPoints[1], SetOfPoints[2])],                       #Find we to start
                Depth)                                                                  #And the deep level

        DrawTheTriangle (
                [SetOfPoints[2],                                                        #Find we to start
                FindMiddlePoint(SetOfPoints[2], SetOfPoints[1]),                        #Find we to start
                FindMiddlePoint(SetOfPoints[0], SetOfPoints[2])],                       #Find we to start
                Depth)                                                                  #And the deep level



DrawTheTriangle(SetOfPoints, 6)                                                         #Teh Function call, this is where all begins



