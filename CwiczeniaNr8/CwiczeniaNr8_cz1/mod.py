s = "Data science."
a = [100, 200, 300]


def foo(arg):
    print(f'arg = {arg}')


class Foo:
    pass


if __name__ == '__main__':
    print(s)
print(a)
foo('XYZ')
x = Foo()
print(x)
