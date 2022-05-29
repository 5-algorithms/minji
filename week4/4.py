#boj 2941
import sys
sys.stdin = open('sample.txt', 'r')

word = input()
special_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=','z=']

cnt = len(word)
for i in range(len(word)-1):
    if word[i:i+2] in special_char:
        cnt -= 1

for i in range(len(word)-2):
    if word[i:i+3] in special_char:
        cnt -= 1

print(cnt)
