x = int(input("Wprowadz liczbę: "))
y = 0
for i in range(x + 1):
    if i % 2 == 1:
        y += i
print("Suma liczb nieparzystych od 1 do ", x, " to: ", y)
