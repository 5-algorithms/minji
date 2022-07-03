import sys
input = sys.stdin.readline
n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

def binary_search(data, start, end):
    while start <= end:
        mid = (start+end)//2
        current = data[0]
        count = 1

        for i in range(1, len(data)):
            if data[i] >= current + mid:
                count += 1
                current = data[i]
        
        if count >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid-1
    return answer

start = 1
end = data[-1] - data[0]
print(binary_search(data, start, end))