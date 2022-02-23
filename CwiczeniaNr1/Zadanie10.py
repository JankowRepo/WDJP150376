x = input("Podaj słowo: ")
y = x[0]
z = x[-1]
x = z + x[1:-1] + y
print(x)
