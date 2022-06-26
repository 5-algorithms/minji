def solution(id_list, report, k):
    answer = []
    over_k = []
    warning = {}
    
    for item in id_list:
        warning[item] = [0, set([])]
    
    for item in report:
        a, b = item.split()    
        if b in warning[a][1]:
            continue
        else:
            warning[a][1].add(b)
            warning[b][0] += 1
            if warning[b][0] >= k:
                over_k.append(b)
    over_k = set(over_k)
    
    for i, e in warning.items():
        answer.append(len(e[1] & over_k))
    
    return answer