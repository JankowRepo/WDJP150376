from collections import namedtuple

Book = namedtuple('Book', ['title', 'price'])


def fun1(book):
    return len(book.title)


def fun2(list_of_books):
    answer = 0
    for book in list_of_books:
        if book.price > answer:
            answer = book.price
    return answer
