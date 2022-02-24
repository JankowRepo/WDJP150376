import math

x = int(input("Wprowadz liczbę pierwszą: "))
y = int(input("Wprowadz liczbę drugą: "))
z = int(input("Wprowadz liczbę trzecią: "))

obwod=x+z+y

print("Obwód trójkąta to: ", obwod)
print("Pole trójkąta to: ", math.sqrt(obwod * (obwod - x) * (obwod - y) * (obwod - z)))