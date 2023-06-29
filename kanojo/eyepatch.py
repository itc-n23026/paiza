def find_books_to_buy():
    N = int(input())
    M1 = int(input())
    your_books = set(map(int, input().split()))
    M2 = int(input())
    bookstore_books = set(map(int, input().split()))

    books_to_buy = sorted(bookstore_books.difference(your_books))

    if len(books_to_buy) == 0:
        return "None"
    else:
        return " ".join(map(str, books_to_buy))


output = find_books_to_buy()
print(output)
