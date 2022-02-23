import math

x = int(input("Wprowadz liczbę pierwszą: "))
y = int(input("Wprowadz liczbę drugą: "))
z = int(input("Wprowadz liczbę trzecią: "))
print("Średnia arytmetyczna: ", (x + y + z) / 3)
print("Średnia geometryczna: ", math.pow((x * y * z), 1 / 3))
