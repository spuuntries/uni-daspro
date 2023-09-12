inp = int(input())

val = {"250": 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0}
# val = {"250": 0, "100": 0, "50": 0, "3": 0, "20": 0, "10": 0, "5": 0}

val_s = sorted(
    val.items(), key=lambda x: int(x[0]), reverse=True
)  # Disort, biar sesuai dgn algo
val = dict(val_s)

for e in val.keys():
    if inp == 0:
        break
    else:
        dv = inp // int(e)
        val[e] = dv
        inp = inp - int(e) * dv

if inp != 0:
    print("Harganya jelek :(")
else:
    for e in dict.items(val):
        print(f"{e[1]} lembar {e[0]} ribuan")
