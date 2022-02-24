x = int(input("Wprowadz sekundy: "))
y = int(input("Wprowadz minuty: "))
z = int(input("Wprowadz godziny: "))

if x>=0 and x<60 and y>=0 and y<60 and z>=0 and z<24:
    print("Taki czas istnieje")
else:
    print("Taki czas nie istnieje")