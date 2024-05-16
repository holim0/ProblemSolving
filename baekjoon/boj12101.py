n, k = map(int, input().split())

answer= []
def find(cur, cur_str):
    
    if cur == n:
        answer.append(cur_str)
        return

    for i in range(1, 4):
        if cur + i <=n:
            find(cur+i, cur_str+"+"+str(i))

max_limit = min(3, n)

for i in range(1, max_limit+1):
    find(i, str(i))

answer= sorted(answer)

if k > len(answer):
    print(-1)
else:
    print(answer[k-1])