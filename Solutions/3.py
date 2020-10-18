# Program to Add Two Integers

def isNumber(num):
    if(type(num) == type(1)):
        return True
    else:
        return False

def add(num1, num2):
    if(isNumber(num1) & isNumber(num2)):
        return num1 + num2
    else:
        return "we only accept numbers."

# Test cases
print(add(1, 2))
print(add("hola", 1))
