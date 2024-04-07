import sys
w, n= map(int, sys.stdin.readline().split())
bobul =[]
answer = 0
for _ in range(n):
    m, p = map(int, sys.stdin.readline().split())
    bobul.append((m, p))
    
bobul = sorted(bobul, key = lambda x : -x[1])

for cur_w, cost in bobul:
    if w == 0: break
    if cur_w <=w:
        answer += (cur_w * cost)
        w -= cur_w
    else:
        answer += (w * cost)
        w = 0
print(answer)