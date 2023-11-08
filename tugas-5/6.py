n = int(input())


# Find shortest route to 1
def find_route(n, t=0):
    if n == 1:
        return t
    routes = []
    if n % 3 == 0:
        routes.append(n // 3)
    if n % 2 == 0:
        routes.append(n // 2)
    routes.append(n - 1)
    return find_route(min(routes), t + 1)


print(find_route(n))
