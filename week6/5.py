def solution(p):
    answer = [0] * len(p)
    for i in range(len(p) - 1):
        smallest = i
        for j in range(i, len(p)):
            if p[smallest] > p[j]:
                smallest = j
        if i != smallest:
            p[i], p[smallest] = p[smallest], p[i]
            answer[i] += 1
            answer[smallest] += 1
    return answer