# Module  : weightconverter.py
# Author  : by Tanya Genao
# Created : 04.22.2019
# A program that converts pounds into grams,kilograms,ounces.



from graphics import *
import tkinter
from tkinter.constants import *
from math import *

def wconverter():
    '''Creates the window and set the background color'''
    win = GraphWin('Weight Converter', 450, 425)
    win.setBackground("grey")

    '''Creates the tittle of the weight converter, size,style and color'''
    center = Point(240,50)
    label = Text(center, "Weight Converter")
    label.setSize(25)
    label.setStyle("bold")
    label.setFill("black")
    label.draw(win)

    '''Creates the box to input pounds and color'''
    box1 = Entry(Point(240,100), 30)
    box1.setFill("white")
    box1.draw(win)

    '''Creates the pounds 'lb' label, size, style and color'''
    center = Point(390,100)
    label2 = Text(center, "lb")
    label2.setSize(12)
    label2.setStyle("bold")
    label2.setFill("black")
    label2.draw(win)

    '''Creates the Grams label, size, style and color'''
    center = Point(132,170)
    label3 = Text(center, "Grams")
    label3.setSize(10)
    label3.setFill("black")
    label3.draw(win)
 
    '''Creates the box for Grams, size and color'''
    box2 = Entry(Point(240, 200), 30)
    box2.setText("0.00")
    box2.setFill("light grey")
    box2.draw(win)

    '''Creates the Kilograms label, size, style and color'''
    center = Point(140,240)
    label4 = Text(center, "Kilograms")
    label4.setSize(10)
    label4.setFill("black")
    label4.draw(win)

    '''Creates the box for Kilograms, size and color'''
    box3 = Entry(Point(240, 270), 30)
    box3.setText("0.00")
    box3.setFill("light grey")
    box3.draw(win)

    '''Creates the Ounces label, size, style and color'''
    center = Point(135,310)
    label5 = Text(center, "Ounces")
    label5.setSize(10)
    label5.setFill("black")
    label5.draw(win)

    '''Creates the box for the Ounces, size and color'''
    box4 = Entry(Point(240, 340), 30)
    box4.setText("0.00")
    box4.setFill("light grey")
    box4.draw(win)
    
    
    '''Creates the rectangle for the 'convert' button and color'''
    button = Rectangle(Point(275,360),Point(375,390))
    button.setFill("orange")
    button.setOutline("orange")
    button.draw(win)
    
    '''create the convert button font size, style and color'''
    buttontxt = Text(Point(325, 375), "Convert")
    buttontxt.setSize(11)
    buttontxt.setStyle("normal")
    buttontxt.setFill("white")
    buttontxt.draw(win)
    win.getMouse()
    
    '''
    Functions for the convertion decision of the mass value input into grams,kilograms,ounce
    and while loop condition if is true or else     
    '''
    def decision():
        '''
        Input   : Mass value in pounds(lb)
        Process : Convertion of pounds(lb) into grams,kilograms and ounces
        Output  : Mass value converted into Grams, Kilograms and Ounces
        '''
        while True:
            
            pounds = float(box1.getText())
            
            if pounds >= 0:
                grams = pounds * 453.59237
                box2.setText(round(grams,3))
                win.getMouse()
                
                kilograms = pounds * .45359237
                box3.setText(round(kilograms,3))
                win.getMouse
                
                ounces = pounds * 16
                box4.setText(round(ounces,3))
                win.getMouse()

                print("Grams is", (round(grams,3)))
                print("Kilograms is",(round(kilograms,3)))
                print("Ounces is",(round(ounces,3)))

            else:
                entry1.setText("INVAILD INPUT,PLEASE enter a NUMBER under the entry.")
                                
                print("INVALID INPUT", "Please enter a NUMBER under the entry")
    decision()

wconverter()    


                


                

