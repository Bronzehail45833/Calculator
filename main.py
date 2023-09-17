from james import Calculator

num1 = float(input("ENTER IN first number: "))
num2= float(input("ENTER IN SECOND number: "))

calculator = Calculator(num1, num2)


operation = str(input("What Operation would you like? +, -, * or / "))

if operation == "+":
    calculator.add(num1,num2)
elif operation == "-":
    calculator.sub(num1,num2)
elif operation == "*":
    calculator.multi(num1,num2)
elif operation == "/":
    calculator.div(num1,num2)
else:
    print("invalid operation")

calculator.GetResult()

