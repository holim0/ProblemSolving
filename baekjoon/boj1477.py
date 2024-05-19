n, m, l = map(int, input().split())

s, e = 1, l

stop = list(map(int, input().split()))

stop.insert(0, 0)
stop.append(l)
stop = sorted(stop)
answer = l-2
def check(diff):

    cnt = 0
    
    for i in range(len(stop)-1):
        
        cur_diff = stop[i+1] - stop[i]-1
        if cur_diff>= diff:
            cnt+= (cur_diff//diff)
    return cnt
                

while s<=e:

    mid = (s+e)//2
    if check(mid) > m:
        s = mid+1

    else:
        e = mid-1
        
print(s)