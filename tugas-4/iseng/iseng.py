key = list(input())
n = int(input())
inputs = [input() for _ in range(n)]

s_key = {}

for i in range(len(key)):
    s_key[key[i]] = key[i + 1 if i + 1 < len(key) - 1 else 0]


for inp in inputs:
    print(
        "".join(
            map(
                lambda x: s_key[x] if x in s_key else x,
                list(inp),
            )
        )
    )
