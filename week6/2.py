def solution(periods, payments, estimates):
    answer = [0, 0]
    cands = []
    for i in range(len(periods)):
        if periods[i] >= 23:
            cands.append(i)
    for cand in cands:
        thismonth = sum(payments[cand])
        nextmonth = thismonth - payments[cand][0] + estimates[cand]
        if periods[cand] == 23 and nextmonth >= 900000:
            answer[0] += 1
        elif 23 < periods[cand] < 59:
            if thismonth < 900000 and nextmonth >= 900000:
                answer[0] += 1
            elif thismonth >= 900000 and nextmonth < 900000:
                answer[1] += 1
        elif periods[cand] == 59:
            if thismonth < 900000 and nextmonth >= 600000:
                answer[0] += 1
            elif thismonth >= 900000 and nextmonth < 600000:
                answer[1] += 1
        else:
            if thismonth < 600000 and nextmonth >= 600000:
                answer[0] += 1
            elif thismonth >= 600000 and nextmonth < 600000:
                answer[1] += 1
    return answer