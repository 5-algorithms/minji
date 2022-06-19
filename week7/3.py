def solution(indices, K):
    d = len(indices) // K
    kfold = [indices[i*d:(i+1)*d] for i in range(K)]
    i = 0
    for x in indices[K*d:]:
        kfold[i].append(x)
        i += 1

    answer = []
    for i in range(2*K):
        cur = i//2
        if i%2 != 0:
            answer.append(kfold[cur])
        else:
            temp = []
            for l, x in enumerate(kfold):
                if l != cur:
                    temp.extend(x)
            answer.append(temp)
    return answer