def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
for num in squares(a, b):
    print(num)