# boj 25115
import math

n = int(input())
items = list(map(int, input().split()))
cash=0

if items[-1]/0.1 < sum(items[:-1]):
    for i in range(n):
        cash += items[i]*(0.1**(n-i) - 1)
    print(math.ceil(cash/(0.1-1)))

else:
    for i in range(n-1):
        cash += items[i]
    res = items[-1] - 0.1*cash
    print(math.ceil(cash+res))