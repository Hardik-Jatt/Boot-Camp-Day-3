def divide(x, y):
    try:
        value = 50
        x.append(value)
    except AttributeError as atr_err:
        print(atr_err)
    else:
        try:
            result = [i / y for i in x]
            print(result)
        except ZeroDivisionError:
            print("Please change 'y' argument to non-zero value")
    finally:
        print("\033[92m Code by Hardik\033[00m")

x = [40, 65, 70, 87]
divide(x, 3)