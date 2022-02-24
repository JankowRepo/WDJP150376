x = int(input("Wprowadz liczbę a: "))
y = int(input("Wprowadz liczbę b: "))
try:
    z = -y / x
    print("X jes równy: ", z)
except:
    print("Dzielenie przez zero!")
