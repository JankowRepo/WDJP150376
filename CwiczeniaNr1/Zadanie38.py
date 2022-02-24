x = int(input("Wprowadz dzień: "))
y = int(input("Wprowadz miesiąc: "))
z = int(input("Wprowadz rok: "))

dzien = False

if 0 < x < 32 and y % 2 == 1:
    dzien = True
elif 0 < x < 29 and y == 2 and z % 4 != 0:
    dzien = True
elif 0 < x < 30 and y == 2 and z % 4 == 0:
    dzien = True
elif 0 < x < 31 and y % 2 == 0 and y != 2:
    dzien = True

miesiac = False
if y < 12 and y > 0:
    miesiac = True

if dzien == True and miesiac == True:
    print("Taka data istnieje")
else:
    print("Taka data nie istnieje")
