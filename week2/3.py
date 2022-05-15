def solution(replies, n, k):
    answer = []

    def check(reply, n, k):
        for i in range(n, len(reply)//2+1):
            for start in range(len(reply)-i*k+1):
                if reply[start:start+i*k] == reply[start:start+i]*k:
                    return False
        return True

    for reply in replies:
        if check(reply, n, k):
            answer.append(1)
        else:
            answer.append(0)

    return answer