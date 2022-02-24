x = int(input("Wprowadz liczbę: "))
wynik = 0
for i in range(x):
    for j in range(i + 1):
        if j == 0 or i == 0:
            wynik = float(1)
        else:
            wynik = wynik * (i - j + 1) / j
        print(wynik, " ", end='')
    print()
