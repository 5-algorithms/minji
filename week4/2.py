# boj 1484
g = int(input())

data = list(range(1,50001))
n = len(data)

start, end = 0, 1
answers = []

while start < end and end < n:
    weight = data[end]**2 - data[start]**2
    if weight == g:
        answers.append(data[end])
    
    if weight < g:
        end += 1
    else:
        start += 1

if answers:
    answers.sort()
    for answer in answers:
        print(answer)
else:
    print(-1)
