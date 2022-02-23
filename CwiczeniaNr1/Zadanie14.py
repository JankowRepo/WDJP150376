def licznik(n):
    suma = 0
    while n > 0:
        x = n % 10
        suma += x
        n = n - x
        n = n / 10

    return suma


print(licznik(54))
