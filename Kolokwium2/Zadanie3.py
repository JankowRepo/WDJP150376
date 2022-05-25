import random
import string
from collections import Counter


def fun1(my_string):
    ch = random.choice(string.ascii_lowercase)
    print("Wylosowana litera: ", ch)
    print("Ilość wystąpień tej litery w zdaniu '", my_string, "': ", Counter(my_string)[ch])


def fun2(number):
    if number < 0 or number > 10 ** 6 or type(number) != int:
        return "Podaj inną liczbę"
    else:
        x = random.randint(0, 9)
        print("Wylosowana liczba to: ", x)
        number_as_string = str(number)
        final_number = int(number_as_string.replace(str(x), ''))
        return final_number
