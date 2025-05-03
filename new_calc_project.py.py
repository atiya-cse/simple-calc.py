def calc():
    a = float(input("Enter a number: "))
    b = float(input("Enter b number: "))
    o = input("Enter an operator(+, -, *, /, //, **, %)")

    if o == "+":
        r = a+b
    elif o == "-":
        r = a-b
    elif o == "*":
        r = a*b
    elif o == "/":
        r = a/b
    elif o == "//":
        r = a//b
    elif o == "**":
        r = a**b
    elif o == "%":
        r = a%b
    else:
        r = "Invalid operation"
    print("Result is:=", r)

calc()