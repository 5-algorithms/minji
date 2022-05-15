# boj 2798

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

combs = combinations(cards, 3)

answer = -1
for comb in combs:
    if sum(comb) > m:
        continue
    else:
        answer = max(answer, sum(comb))

print(answer)