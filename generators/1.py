def square_generator(n):
    for i in range(1, n+1):
        yield i ** 2
n = int(input("Input number: "))
squares = square_generator(n)
for square in squares:
    print(square)