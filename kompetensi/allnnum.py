n = int(input())
print(
    " ".join(
        map(str, list(filter(lambda x: x % 2 == 0, [n for n in range(1, n + 1)])))
    ),
    end="",
)
