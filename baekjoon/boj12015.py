n = int(input())

number = list(map(int, input().split()))
number.insert(0, 0)
INF = 1e10
dp = [INF, number[1]]


for i in range(2, n+1):
    if number[i] > dp[-1]:
        dp.append(number[i])

    else:
        s, e = 1, len(dp)-1
        isBreak= False
        while s<=e:
            mid = (s+e)//2

            if dp[mid] == number[i]:
                isBreak = True
                break
            elif dp[mid]< number[i]:
                s = mid+1
            else:
                e = mid-1
        if not isBreak:
            dp[s] = number[i]

print(len(dp)-1)
            





