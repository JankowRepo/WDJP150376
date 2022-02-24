x = int(input("Wprowadz liczbę : "))
for i in range(x, 0, -1):
    for j in range(i):
        print(x, end='')
    print()
