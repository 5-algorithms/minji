t = int(input())

house = [list(range(15))]

for floor in range(1, 15):
    house.append([])
    for i in range(15):
        house[-1].append(sum(house[floor-1][:i+1]))

for _ in range(t):
    k = int(input())
    n = int(input())
    print(house[k][n])
