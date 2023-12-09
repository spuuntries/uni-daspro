n = int(input())
inputs = [input() for _ in range(n)]
ns = int(input())
swaps = [input().split() for _ in range(ns)]

for s in swaps:
    if s[0] in inputs and s[1] in inputs:
        h1 = inputs.index(s[0])
        h2 = inputs.index(s[1])
        inputs[h1] = s[1]
        inputs[h2] = s[0]

[print(h) for h in inputs]
