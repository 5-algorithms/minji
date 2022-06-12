# boj 1308
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def count_days(y1, m1, d1, m2, d2, months):
    days = 0
    yunnyeon = False
    if y1%400 == 0:
        yunnyeon = True
    elif y1 % 4 == 0 and y1 % 100 != 0:
        yunnyeon = True
    if yunnyeon:
        months[2] = 29
    days = 0
    if m1 == m2:
        days += d2-d1
    else:
        days += months[m1] - d1
        for month in range(m1+1, m2):
            days += months[month]
        days += d2
    return days

if m2 >= m1 and d2 >= d1 and y2-y1 >= 10000:
    print("gg")
else:
    if y1 == y2:
        days = count_days(y1, m1, d1, m2, d2, months)
    else:
        days = count_days(y1, m1, d1, 12, 31, months)
        days += 1
        for year in range(y1 + 1, y2):
            days += count_days(year, 1, 1, 12, 31, months)
            days += 1
        days += count_days(y2, 1, 1, m2, d2, months)
    print(f"D-{days}")