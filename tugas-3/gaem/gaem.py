inp = int(input())
inp += 1 if inp % 2 != 0 else 0  # n+=1 kalau ganjil.

mon = {
    "slime": {"count": 0, "hp": 3, "xp": 6},
    "hilichurl": {"count": 0, "hp": 4, "xp": 8},
    "abyss mage": {"count": 0, "hp": 5, "xp": 10},
}

mon = list(
    sorted(mon.items(), key=lambda x: x[1]["xp"], reverse=True)
)  # Sort berdasarkan xp

# Credit algoritma (disini dirapihin aja): Addin (Shalahuddin Ahmad Cahyoga)
tot = 0

for i, e in enumerate(mon):  # Untuk tiap monster
    dinp = inp // e[1]["xp"]  # Bagi habis total
    mon[i][1]["count"] = dinp  # Jumlah monster = hasil bagi

    tot += dinp * e[1]["hp"]  # Total serangan += hasil bagi * hp

    inp -= dinp * e[1]["xp"]  # Total xp -= hasil bagi * xp monster

if (
    inp > 0
):  # Kalo total xp masih sisa, pasti 0 < n < 6, jumlah slime (pokoknya yg paling kecil) + 1
    mon[-1][1]["count"] += 1

print(tot)
mon.reverse()
for e in mon:
    print(e[1]["count"])
