n = int(input())


# Find shortest route to 1
def find_route(n, t=0):
    if n == 1:
        return t
    if n % 3 == 0:
        return find_route(n // 3, t + 1)
    if n % 2 == 0:
        return find_route(n // 2, t + 1)
    return find_route(n - 1, t + 1)


print(find_route(n))
