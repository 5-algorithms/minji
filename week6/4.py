#boj 17478
q = int(input())

answer = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n"
t = ""
count = 0

def professor(count, answer, t):
    if count > 0:
        t += "____"
    if count < q:
        answer += f'{t}"재귀함수가 뭔가요?"\n{t}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n{t}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n{t}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n'
        answer = professor(count + 1, answer, t)
        answer += f"{t}라고 답변하였지.\n"
        return answer
    else:
        end = f'{t}"재귀함수가 뭔가요?"\n{t}"재귀함수는 자기 자신을 호출하는 함수라네"\n{t}라고 답변하였지.\n'
        answer += end
        return answer

print(professor(count, answer, t))