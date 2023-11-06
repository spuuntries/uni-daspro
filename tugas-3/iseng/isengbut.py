key = list(input())
n = int(input())
inputs = [list(input()) for _ in range(n)]


for inp in inputs:
    normal = "abcdefghijklmnopqrstuvwxyz"
    print("".join([key[normal.index(c)] if c in normal else c for c in inp]))
