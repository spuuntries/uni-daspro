n = int(input())
res = "A"
if 0 <= n <= 40:
    res = "E"
elif 41 <= n <= 55:
    res = "D"
elif 56 <= n <= 60:
    res = "C"
elif 61 <= n <= 65:
    res = "BC"
elif 66 <= n <= 75:
    res = "B"
elif 76 <= n <= 85:
    res = "AB"
elif 86 <= n <= 100:
    res = "A"
print(res)
