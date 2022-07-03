t = int(input())

def solution(word, r):
    answer = ''
    for c in word:
        answer += c*r
    return answer

for _ in range(t):
    r, word = input().split()
    print(solution(word, int(r)))