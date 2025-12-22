y = float(input("first number: "))
op = input("operation (+, -, *, /): ")
t = float(input("second number: "))
if op == "+":
    print(y+t)
elif op == "-":
    print(y-t)
elif op == "*":
    print(y*t)
elif op == "/":
    if t == 0:
        print("cannot do this operation")
    else:
        print(y/t)
else:
    print("unknow operation")
