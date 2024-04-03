import sys
n, m = map(int, input().split())

namu = list(map(int, input().split()))

start = 1
end = max(namu)

answer = 1

while start <= end:
    
    mid = (start+end)//2

    cur_len = 0

    for value in namu:
        if value >= mid:
            cur_len += (value-mid)
    
    if cur_len>=m:
        start = mid + 1

    
    elif cur_len<m:
        end = mid -1

print(end)