import re
import math

_ = input()
days = [int(n) for n in re.split(r" +", input())]
last = input()

day = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

print(day[(day.index(last) + math.lcm(*days)) % 7])
