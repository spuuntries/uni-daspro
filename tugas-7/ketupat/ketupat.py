n = int(input())
s = " "

for m in range(n):
    print(s * (n - m), end="")
    if m != n:
        print(s * (n - m), end="")
    if m:
        for i in range(m):
            print(i, end=" ")
        for i in range(m, -1, -1):
            print(i, end=" ")
    else:
        print(0, end="")
    print()

for m in range(n, -1, -1):
    print(s * (n - m), end="")
    if m != n:
        print(s * (n - m), end="")
    if m:
        for i in range(m):
            print(i, end=" ")
        for i in range(m, -1, -1):
            print(i, end=" ")
    else:
        print(0, end="")
    print()
