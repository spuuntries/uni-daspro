import re


# Algo Tomohiko Sakamoto
def tomoSaka(y, m, d):
    g = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if m < 3:
        y -= 1

    return (y + y // 4 - y // 100 + y // 400 + g[m - 1] + d) % 7


inp = [int(e) for e in re.split(r" +", input())]
mo = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
]
da = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

print(f"Tanggal : {inp[0]} {mo[inp[1]-1]} {inp[2]}")
print(f"Hari : {da[tomoSaka(inp[2], inp[1], inp[0])-1]}")
