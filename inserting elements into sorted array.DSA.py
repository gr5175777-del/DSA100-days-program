x = int(input("enter first number:"))
y = int(input("enter second number:"))
ch = input("enter operator(+,,-,*,/,%):")

if ch == "+":
    print(x+y)
elif ch == "-":
    print(x-y)
elif  ch == "*":
    print(x*y)
elif ch == "/":
    print(x/y)
elif ch == "%":
    print(x%y)
else:
    print("enter valid operator")
  