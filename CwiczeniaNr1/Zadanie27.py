import math

x = int(input("Wprowadz promień: "))
y = int(input("Wprowadz bok stożka: "))
z = int(input("Wprowadz wysokość stożka: "))

print("Pole powierzchni stożka to: ", math.pi * x * (x + y))
print("Objętość stożka to: ", (math.pi * x * x * z) / 3)
