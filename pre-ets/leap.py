import re


def leap(y):
    return [False, True].index(y % 4 == 0 and (y % 100 > 0 or y % 400 == 0))


def day(m, d, y):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = 0
    if [False, True][leap(y)] and m > 2:
        res += 1
    res += sum(days[0:m])
    res -= days[m - 1] - d
    return res


monthmap = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

print(
    day(
        *[
            (monthmap.index(e[1]) + 1) if e[0] == 0 else int(e[1])
            for e in enumerate(re.split(" +", input().replace(",", "")))
        ]
    )
)

# Yang di atas bentuk pendek dari:
# inputlist = []
# for i, e in enumerate(input().replace(",", "").split()):
#     if i == 0:
#         inputlist.append(monthmap.index(e) + 1)
#     else:
#         inputlist.append(int(e))
# print(day(*inputlist))
