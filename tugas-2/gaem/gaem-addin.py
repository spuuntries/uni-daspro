# Implementasi Addin
n = int(input())  # exp yang diperlukan

if (n % 2) != 0:  # untuk exp yang ganjil
    n = n + 1  # digenapkan ke atas

abyss_mage = n // 10  # satu abyss mage per 10 exp
n = n - (abyss_mage * 10)  # dikurangi exp dari abyss mage
hilichurl = n // 8  # diulang untuk hilichurl & slime
n = n - (hilichurl * 8)
slime = n // 6
n = n - (slime * 6)

if n != 0:  # untuk sisa (pasti 0<n<6)
    slime = slime + 1

totalserang = (
    (abyss_mage * 5) + (hilichurl * 4) + (slime * 3)
)  # menghitung total serangan

print(
    f"Jumlah total serangan minimal yang harus dikeluarkan Gaem : {totalserang}"
)  # output/keluaran
print(f"Jumlah Slime yang harus dikalahkan Gaem : {slime}")
print(f"Jumlah Hilichurl yang harus dikalahkan Gaem : {hilichurl}")
print(f"Jumlah Abyss Mage yang harus dikalahkan Gaem : {abyss_mage}")
