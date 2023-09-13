# Agak ngechit pake datetime, datetime built-in kan tapi 🙏

import datetime
import re

inp = [int(e) for e in re.split(r" +", input())]
inp.reverse()
inp = datetime.datetime(*inp)
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

print(f"Tanggal : {inp.day} {mo[inp.month-1]} {inp.year}")
print(f"Hari : {da[inp.weekday()]}")
