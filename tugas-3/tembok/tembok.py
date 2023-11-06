inputs = []

while True:
    inp = input().replace("\n", "")
    if inp[-1] == "":
        inputs.append(int(inp.replace("", "")))
        break

    inputs.append(int(inp))


def solve(N):
    f = [0, 1, 5, 11] + [0] * N

    for i in range(4, N + 1):
        f[i] = f[i - 1] + 4 * f[i - 2] + 2 * f[i - 3]

    return f[N]


for N in inputs:
    print(solve(N))
