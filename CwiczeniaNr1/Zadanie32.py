x = int(input("Wprowadz liczbę: "))
y = int(input("Wprowadz drugą liczbę: "))
z = int(input("Wprowadz trzecią liczbę: "))

lista = [x, y, z]
for j in range(len(lista)):
    for i in range(len(lista) - 1):
        if lista[i] < lista[i+1]:
            tmp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = tmp

print(lista[0])
print(lista[1])
print(lista[2])
