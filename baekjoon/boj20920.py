import sys
n, m = map(int, input().split())
input = sys.stdin.readline
word = []

for i in range(n):
    w = input().rstrip()

    if len(w)>=m:
        word.append(w)

cnt = {}

for w in word:
    if w not in cnt:
        cnt[w] = 1
    else:
        cnt[w] +=1

cnt = sorted(cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

answer = cnt



for value, cnt in answer:
    print(value)    

        


