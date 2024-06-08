try:
    print(1 / 0)
except ZeroDivisionError:
    print("You cannot divide a value with zero")
except Exception:
    print("Something else went wrong")

try:
    print(x)
except NameError:
    print("Variable not defined")