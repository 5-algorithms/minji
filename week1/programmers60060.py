from bisect import bisect_left

def bisect_right_prefix(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid] and not a[mid].startswith(x): hi = mid
        else: lo = mid+1
    return lo

def solution(words, queries):
    reverse = [word[::-1] for word in words]
    words.sort()
    reverse.sort()
    answer = []
    arr1 = [[] for _ in range(10001)]
    arr2 = [[] for _ in range(10001)]

    for word in words:
        arr1[len(word)].append(word)
    for word in reverse:
        arr2[len(word)].append(word)

    for query in queries:
        n = len(query)

        if query.startswith('?'):
            end = bisect_right_prefix(query, '?')
            search = query[end:]
            search = search[::-1]
            leftIndex = bisect_left(arr2[n], search)
            rightIndex = bisect_right_prefix(arr2[n], search)
            answer.append(rightIndex-leftIndex)
        else:
            start = query.index('?')
            search = query[:start]
            leftIndex = bisect_left(arr1[n], search)
            rightIndex = bisect_right_prefix(arr1[n], search)
            answer.append(rightIndex-leftIndex)
    return answer