n,m = map(int, input().split())

number = list(map(int, input().split()))

s, e  = 0, max(number)
answer = 1e10

def find(mid):
    global number
    minValue = number[0]
    maxValue = number[0]
    cnt = 1
    for i in range(len(number)):
        maxValue = max(maxValue, number[i])
        minValue = min(minValue, number[i])

        if maxValue - minValue > mid:
            cnt +=1 
            maxValue = minValue = number[i]

    return cnt


while s<=e:

    mid = (s+e)//2


    if find(mid) <=m:
        e = mid -1
        answer = min(mid, answer)
    else:
        s = mid+1

print(answer)