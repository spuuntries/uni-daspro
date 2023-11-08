n = int(input())


# Find shortest route to 1
def find_route(n, t=0):
    if n == 1:
        return t
    route = None
    if n % 3 == 0:
        route = n // 3
    if n % 2 == 0:
        route = n // 2
    if not route:
        route = n - 1
    return find_route(route, t + 1)


print(find_route(n))
