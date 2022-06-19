def solution(blocks):
    f1, f2 = 0, 0
    answer = 0
    n = len(blocks)

    while f1 < n and f2 < n:
        count = 0
        block = blocks[f1]
        for i in range(f1-1, -1, -1):
            if blocks[i] >= block:
                count += 1
                block = blocks[i]
            else:
                break
        block = blocks[f2]
        for i in range(f2, n):
            if blocks[i] >= block:
                count += 1
                block = blocks[i]
                if i == n-1:
                    f1, f2 = n, n
            else:
                f1, f2 = i, i
                break
        answer = max(answer, count)

    return answer