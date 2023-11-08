n = int(input())
c = "*"

print(c)


def gunung(n):
    if n >= 2:
        gunung(n - 1)
        print(c * n)
        print(c)
        gunung(n - 1)


gunung(n)
