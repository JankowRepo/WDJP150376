x = int(input("Wprowadz liczbę pierwszą: "))
y = int(input("Wprowadz liczbę drugą: "))
z = int(input("Wprowadz liczbę trzecią: "))
wynik = 0
if x > y:
    wynik = x
else:
    wynik = y
if z > wynik:
    wynik = z
print("Największa liczba wynosi: ", wynik)
