import sys
input = sys.stdin.readline
n = int(input())
half = list(map(int, input().split()))
answer = 0
limit = max(half)
for i in range(2, limit+1):
    cur_value = i
    cnt = 0
    for h in half:
        if cur_value<=h and h%cur_value==0:
            cnt+=1
    answer = max(answer, cnt)
    
print(answer)