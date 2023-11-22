n = int(input())
c = "*"

base = c * 2 if n % 2 == 0 else c

print(base)


def gunung(n):
    if n > len(base):
        gunung(n - 2)
        print(c * n)
        print(base)
        gunung(n - 2)


gunung(n)
