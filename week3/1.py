# boj 1644
n = int(input())

k = 4000000
a = [False, False] + [True] * (k-1)
primes = []

for i in range(2, k):
    if a[i]:
        primes.append(i)
        for j in range(2, k//i + 1):
            a[i*j] = False

start = 0
end = 0
count = 0

while start <= end and primes[start] <= n:
    if sum(primes[start:end+1]) == n:
        count += 1
        
    if end == len(primes)-1:
        start += 1
        continue
    
    if sum(primes[start:end+1]) < n:
        end += 1
    else:
        start += 1

print(count)
