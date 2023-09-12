inp = int(input())
day = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]


# Algo Tomohiko Sakamoto
def tomoSaka(y, m, d):
    g = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if m < 3:
        y -= 1

    return (y + y // 4 - y // 100 + y // 400 + g[m - 1] + d) % 7


print(day[tomoSaka(inp - 1, 12, 31) - 1])
