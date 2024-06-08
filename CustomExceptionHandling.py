try:
    if value > 1_000:
        raise ValueError("Please add a value lower than 1,000")
    else:
        print("Congratulations You are the winner!!")
except ValueError as e:
    print(e)

value = 2_000