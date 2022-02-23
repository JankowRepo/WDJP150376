def licznik(n):
    suma = 0
    for i in range(1, n + 1):
        if n % i == 0:
            suma += suma + 1
    return suma


print(licznik(100))
