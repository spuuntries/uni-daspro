m, n = map(int, input().split())
_ = input()
items = list(map(int, input().split()))


def can(x, m, n):  # This is based on the Frobenius Number, a bit tough, but look into the McNuggets problem.
    return (
        m * n - m - n < x
        or x % m == 0
        or x % n == 0
        or x % m % n == 0
        or x % n % m == 0
    )


print(
    " ".join(map(str, sorted(filter(lambda x: can(x, m, n), items), reverse=True)[:3]))
)
