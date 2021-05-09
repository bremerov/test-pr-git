def addNumbers(num1,num2):
    return num1 + num2

def substractNumbers(num1,num2):
    return num1 - num2

def productNumbers(num1,num2):
    return num1 * num2

def divideNumbers(num1,num2):
    return num1 / num2

def divideThreeNumbers(num1,num2, num3):
    return (num1 / num2)/num3

som1=addNumbers(1,4)
som2=substractNumbers(1,4)
print(str(som1 + som2))

divide=divideNumbers(1,4)
divideTwo=divideNumbers(1,4,4)
product=productNumbers(1,4)
print(str(divide + divideTwo + product))