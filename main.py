##### BB kata: Is it a number? #####

#Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

#Valid examples, should return true:
#isDigit("3")
#isDigit("  3  ")
#isDigit("-3.23")

#should return false:
#isDigit("3-4")
#isDigit("  3   5")
#isDigit("3 5")
#isDigit("zero")

#Given string check if it is an INT or FLOAT, if yes then output TRUE otherwise FALSE:

def isDigit(x):
    if x == str(x):
        x = x.strip()   #remove leading/trailing spaces first

    y= x
    if checkINT(y) == True:
        return True

    z=x
    if checkFLOAT(z) == True:
        return True
    else:
        return False

def checkINT(y):
    try:
        int(y)
    except ValueError:
        return False
    y = int(y)
    if y == int(y):
        return True
    
def checkFLOAT(z):
    try:
        float(z)
    except ValueError:
        return False
    z = float(z)
    if z == float(z):    
        return True
    
print(isDigit("   -3.23   "))




##### ND kata: Rock Paper Scissors #####






##### MDM kata: Get Planet Name By ID #####





