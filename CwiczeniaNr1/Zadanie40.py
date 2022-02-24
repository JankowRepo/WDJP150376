x = int(input("Wprowadz 3-cyfrową liczbę całkowitą: "))
y = (x - (x % 10)) / 10
z = (y - (y % 10)) / 10
if x % 10 == z:
    print("Ta liczba to polindrom")
else:
    print("Ta liczba to nie polindrom")
