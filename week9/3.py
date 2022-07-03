n = int(input())

def check(word):
    words_list = []
    for c in word:
        if c not in words_list:
            words_list.append(c)
            cur = c
        else:
            if not cur == c:
                return False
    return True

answer = 0
for _ in range(n):
    if check(input()):
        answer += 1

print(answer)