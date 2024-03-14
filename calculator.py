def sum(op1, op2):
  print("the addition of numbers is : " , op1+op2 )
def sub(op1, op2):
  print("the subtraction of numbers is : " , op1-op2)
def mul(op1, op2):
  print("the multiplication of numbers is : ", op1*op2)
def div(op1, op2):
  print("the division of numbers is : ")
  if op2 == 0:
   print("division is not possible")
  else:
   print("the division of numbers is : " , op1/op2)
def rem(op1, op2):
  print("the remainder of numbers is : " , op1%op2)

def calculator(op1,op2,operation):
   if operation == '+':
    sum(op1,op2)
   elif operation == '-':
    sub(op1,op2)
   elif operation == '*':
    mul(op1,op2)
   elif operation == '/':
    div(op1,op2)
   elif operation == '% ':
    rem(op1,op2)
   else:
    print("invalid operation")
  
op1 = int(input("enter the first number : "))
op2 = int(input("enter the second number : "))
operation = input("enter the operation() : ",)
calculator(op1,op2,operation)
