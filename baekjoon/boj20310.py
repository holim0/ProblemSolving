s = input()
s = list(s)

check = [False] * len(s)
zeroCnt = 0
oneCnt = 0

for ss in s:
    if ss ==  "0":
        zeroCnt+=1
    else:
        oneCnt+=1

zeroCnt/=2
oneCnt/=2

for i in range(len(s)):
    if s[i]== "1":
        if oneCnt>0:
            oneCnt-=1
            check[i] = True
        else:
            break
for i in range(len(s)-1, -1, -1):
    if s[i] == "0":
        if zeroCnt>0:
            zeroCnt-=1
            check[i] = True
        else:
            break

answer= ""
for i in range(len(s)):
    if not check[i]:
        answer+= s[i]

print(answer)