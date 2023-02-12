# a better calculator
num1 = float(input("enter 1st number: "))
op = input("enter operator: ")
num2 = float(input("enter 2nd number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")