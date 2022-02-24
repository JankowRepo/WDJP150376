import math

x = int(input("Wprowadz promień walca: "))
y = int(input("Wprowadz wysokość walca: "))

print("Pole powierzchni walca to: ", 2*math.pi*x*(x+y))
print("Objętość walca to: ", math.pi*x*x*y)
