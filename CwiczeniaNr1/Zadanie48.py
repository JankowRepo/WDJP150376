x = int(input("Wprowadz liczbę: "))
y = 0
for i in range(x + 1):
    if i % 2 == 0:
        y += i
print("Suma liczb parzystych od 1 do ", x, " to: ", y)
