# ==========================================================================
# ==================     FIND ROOT OF COMPLEX NUMBER   =====================
# ==========================================================================
from graphics import *                                                  #Please I will need that
from math import *                                                      #Please I will need that

Pi = 3.141592


# ================================================
# =======   GENERAL COORDINATE DRAWING   =========
# ================================================

Width  = 900                                                            #Size of the drawing window
Heigth = 500                                                            #Size of the drawing window

def GetMathCoordinates(a, b):                                           #Cool function to do it right 
    return [(Width/2 + a), (Heigth/2 - b)]                              #That all folks!
    

def DrawCoodinateSystem (MainWindow, Width, Heigth, ExpandFactor):      #Draw Cartesian Coordinates
    Lines = []                                                          #This will be lines to draw

    for PossibleHeigth in range(Heigth/2, Heigth, ExpandFactor):        #Get All vertical bars
        Up = PossibleHeigth; Down = Heigth-PossibleHeigth;              #This is for shorter names
        Lines.append(Line( Point(10, Up)   , Point(Width-10, Up)   ))   #All positive vertical bars
        Lines.append(Line( Point(10, Down) , Point(Width-10, Down) ))   #All negative vertical bars
    
    for PossibleWidth in range(Width/2, Width, ExpandFactor):           #Get All vertical bars
        Up = PossibleWidth; Down = Width-PossibleWidth;                 #This is for shorter names
        Lines.append(Line( Point(Up, 10)   , Point(Up, Heigth-10)   ))  #All positive horizontal bars
        Lines.append(Line( Point(Down, 10) , Point(Down, Heigth-10) ))  #All negative horizontal bars

    for SomeLine in Lines:                                              #For each line to draw
        SomeLine.setFill(color_rgb(38, 166, 154));                      #Chose a cool color
        SomeLine.draw(MainWindow)                                       #Draw it now!

    XAxis = Line(Point(10, Heigth/2) , Point(Width-10, Heigth/2))       #Principal Axis
    YAxis = Line(Point(Width/2, 10)  , Point(Width/2, Heigth-10))       #Principal Axis

    for Coordinate in [XAxis, YAxis]:                                   #For the axis:
        Coordinate.setArrow("both"); Coordinate.setWidth(5)             #Set an arrow and width
        Coordinate.setFill(color_rgb(0, 131, 143))                      #A different color ;)
        Coordinate.draw(MainWindow)                                     #Show it!



# ================================================
# =======       FIND COMPLEX ROOTS       =========
# ================================================

def FindAngle(a, b):                                                    #Return the correct angle
    if (a > 0): return atan2(b,a)                                       #If 1 or 4 cuadrant
    if (b > 0): return (atan2(b,a) + Pi)                                #If 2 cuadrant
    if (b < 0): return (atan2(b,a) - Pi)                                #If 3 cuadrant

def FindRootsComplex(a, b, n):                                          #Real magic! where z = a+bi
    Solutions = []                                                      #This is where put result
    Module    = sqrt((a*a) + (b*b))                                     #Module of z
    Angle     = FindAngle(a, b)                                         #Angle of z
    Module = Module**(1.0/n)                                            #Module for z^(1/n)

    for nSolution in range(0, n):                                       #For each solution
        RealPart      = Module * cos((Angle + (2*(Pi)*nSolution))/n)    #Find real part
        ImaginarePart = Module * sin((Angle + (2*(Pi)*nSolution))/n)    #Find complex part
        Solutions.append([RealPart, ImaginarePart])                     #Add to solutions
        print RealPart,"+ i",ImaginarePart                              #Maybe send to console to :D

    return Solutions                                                    #We will need this later
    

def ShowSolution(Solutions, MainWindow, ExpandFactor):                  #Show the result we have got!
    for Solution in Solutions:                                          #For each solution
        
        FinalX = (Width/2  + (Solution[0] * ExpandFactor))              #Get them right and expand it!
        FinalY = (Heigth/2 - (Solution[1] * ExpandFactor))              #Get them right and expand it!
        
        OriginPoint = Point(Width/2, Heigth/2)                          #Points, find it
        FinalPoint  = Point(FinalX, FinalY)                             #The real point
        
        CoolVector = Line(OriginPoint, FinalPoint)                      #A vector like solution
        CoolVector.setArrow("last"); CoolVector.setWidth(5)             #Now make it look like vector
        CoolVector.setFill(color_rgb(48, 63, 169))                      #Cool style
        CoolVector.draw(MainWindow)                                     #And show it!

        Title = "(%.3f) + (%.3f)i" % (Solution[0], Solution[1])         #Now get string with solution
        VectorText = Text(FinalPoint, Title)                            #A text to show it
        VectorText.setSize(22); VectorText.setStyle("bold")             #Some style
        VectorText.draw(MainWindow)                                     #Show it!



def main():                                                             #Set all in action
    MainWindow = GraphWin("Find & Draw Roots", Width, Heigth)           #Create a Window

    print "Solution for z = a+bi"                                       #Cool input, that's it       
    a = int(input("Real Part of Z: "))                                  #Cool input, that's it   
    b = int(input("Imaginare Part of Z: "))                             #Cool input, that's it   
    n = int(input("Number of Roots: "))                                 #Cool input, that's it
    
    ExpandFactor = (int)(Heigth / (max([a,b])*2) )                      #Set a ExpandFactor
    print "Expand factor is ",ExpandFactor                              #Show the ExpandFactor

    DrawCoodinateSystem(MainWindow, Width, Heigth, ExpandFactor)        #Draw a coordinate system

    Title = "Solution: [(%i) + (%i)i]^%i" % (a, b, n)                   #Set title for what we will do
    NumberText = Text(Point(Width/2, 30), Title)                        #Set the text to show it
    NumberText.setSize(30); NumberText.setStyle("bold")                 #Style it
    NumberText.draw(MainWindow)                                         #Show it!

    ShowSolution(FindRootsComplex(a, b, n), MainWindow, ExpandFactor);  #Show the Solution

    MainWindow.getMouse()                                               #Pause for click in window
    MainWindow.getMouse()                                               #Pause for 2 click in window
    MainWindow.close()                                                  #Bye good window :'(

main()                                                                  #A function to start them all



