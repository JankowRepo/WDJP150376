def kalkulator(data):
    char = data[1]
    num1 = int(data[0])
    num2 = int(data[2])
    if char == '+':
        return num1 + num2
    elif char == '-':
        return num1 - num2
    elif char == '*':
        return num1 * num2
    elif char == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Nie dziel przez zero!"
    else:
        return "Błędne działanie"


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        print(kalkulator(sys.argv[1:4]))
