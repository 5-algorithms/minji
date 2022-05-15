# boj 2525
h, m = map(int, input().split())
cook = int(input())

cook_h, cook_m = cook // 60, cook % 60

if m + cook_m >= 60:
    m = m + cook_m - 60
    h += 1
else:
    m = m + cook_m

if h + cook_h >= 24:
    h = h + cook_h - 24
else:
    h = h + cook_h

print(h, m)