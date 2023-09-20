import math

n = int(input())
inputs = [int(input()) for _ in range(n)]


def pal(n):
    return str(n) == str(n)[::-1]


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def c_pal(n):
    ip = n
    while True:
        ip += 1
        if pal(ip) and is_prime(ip):
            return ip


for i, inp in enumerate(inputs):
    if pal(inp) and is_prime(inp):
        print(f"#{i+1}: {inp}")
    else:
        print(f"#{i+1}: {c_pal(inp)}")
