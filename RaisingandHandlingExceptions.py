def divide(x, y):
    try:
        if value > 1_000:
            raise Exception("Please add a value lower than 1,000")
        else:
            print("Congratulations You are the winner!!")
    except Exception as e:
        print(e)

value = 2_000
divide(value, 3)