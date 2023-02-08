while True:
    try:
        expression = input()
    except EOFError:
        break

    print(f"{eval(expression):.2f}")
