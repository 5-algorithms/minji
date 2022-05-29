word = input()

Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

answer = 0

for char in word:
    for i, num in enumerate(Number):
        if char in num:
            answer += i + 3

print(answer)
