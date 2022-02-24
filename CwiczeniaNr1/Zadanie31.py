x = int(input("Wprowadz liczbę: "))
y = int(input("Wprowadz drugą liczbę: "))
if x % y != 0:
    print("Liczba jest niepodzielna przez ", y)
    print("Reszta z dzielenia to ", x % y)
else:
    print("Liczba jest podzielna przez ", y)
    print("Reszta z dzielenia to ", x % y)
