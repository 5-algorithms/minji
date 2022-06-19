def solution(S, C):
    columns = S.split("\n")[0].split(',')
    idx = columns.index(C)
    rows = [row.split(',') for row in S.split("\n")[1:]]
    data = [int(row[idx]) for row in rows]
    
    return max(data)
