# v2, agak ngechit pake datetime, datetime built-in kan tapi 🙏

import datetime

inp = int(input())
day = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

print(day[datetime.datetime(inp - 1, 12, 31).weekday()])
