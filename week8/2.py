n = int(input())
div5 = n//5

def solution(n, div5):
    if div5 == 0:
        if n % 3 == 0:
            return n // 3
        else:
            return -1
    
    res = n - 5 * div5
    div3 = res//3
    res -= 3*div3
    if res == 0:
        return(div5+div3)
    else:
        div5 -= 1
        return solution(n, div5)

print(solution(n, div5))