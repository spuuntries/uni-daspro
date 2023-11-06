n = int(input())
inputs = [input() for _ in range(n)]


def pal(n):
    return str(n) == str(n)[::-1]


[print("Mehas pasti suka!" if pal(inp) else "Jangan ini, deh.") for inp in inputs]
