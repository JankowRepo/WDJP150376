import time


def zegar(counter=10):
    print(counter)
    while True:
        time.sleep(1)
        counter -= 1
        print(counter)
        if counter == 0:
            break
    return "Odliczanie zakończyło się!"


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        print(zegar(int(sys.argv[1])))
