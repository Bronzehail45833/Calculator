class Calculator:
    def __init__(self,num1,num2):
     self.num1 = num1
     self.num2 = num2
     self.result = 0

    def add(self,num1,num2):
       self.result = num1 + num2
       self.operation = "addition"

    def sub(self,num1,num2):
       self.result = num1 - num2
       self.operation = "subtraction"


    def multi(self,num1,num2):
       self.result = num1 * num2
       self.operation = "multiplication"


    def div(self,num1,num2):
       self.operation = "division"
       self.result = num1 / num2
       if num1 == 0 or num2 == 0:
          print("error, You cont DIDIVE BY 0 DUMASS")

    def GetResult(self):
       print(f"The result of your {self.operation} is {self.result}")