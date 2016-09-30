'''
    Program: Magical Calculator
    Author: Nick G
    Copyright: 2016

'''


import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True
beenrun = False

def performMath():
    global run
    global previous
    global beenrun
    equation = ""


    # If there has been a previous calculation, use that result as the prompt
    if beenrun == False:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    # if user quits ->
    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if beenrun == False:
            previous = eval(equation)
            beenrun = True
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
