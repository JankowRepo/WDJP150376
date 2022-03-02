x1 = float(input("Wprowadz pierwszą liczbę wymierną: "))
y1 = float(input("Wprowadz drugą liczbę wymierną: "))
x2 = float(input("Wprowadz trzecią liczbę wymierną: "))
y2 = float(input("Wprowadz czwartą liczbę wymierną: "))

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
print(distance)
