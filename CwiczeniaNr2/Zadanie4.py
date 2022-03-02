x = float(input("Wprowadz pierwszą liczbę wymierną: "))
y = float(input("Wprowadz drugą liczbę wymierną: "))
z = float(input("Wprowadz trzecią liczbę wymierną: "))
v = float(input("Wprowadz czwartą liczbę wymierną: "))

mean = (x + y + z + v) / 4
print(mean)

variance = (((x - mean) ** 2) + ((y - mean) ** 2) + ((z - mean) ** 2) + ((v - mean) ** 2)) / 4
print(variance)
