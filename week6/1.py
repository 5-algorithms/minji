#boj 2908
a, b =input().split()
ra, rb = a[::-1], b[::-1]
if int(ra) > int(rb):
    print(ra)
else:
    print(rb)
