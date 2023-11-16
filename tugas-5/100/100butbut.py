p, t = map(int, input().split())


# @profile
# def ways(p, t):
#     if p == 100:
#         return 1
#     elif p > 100:
#         return 0
#     elif p == t:
#         return 0
#     else:
#         res = 0
#         for i in range(1, 7):
#             res += ways(p + i, t)
#         return res


# @profile
def ways(p, t, memo={}):
    if p == 100:
        return 1
    elif p > 100 or p == t:
        return 0
    elif p in memo:
        return memo[p]
    else:
        res = 0
        for i in range(1, 7):
            res += ways(p + i, t, memo)
        memo[p] = res
        return res


res = ways(p, t)
print(f"Ada {res} cara nih!")
