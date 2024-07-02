a, b = input().split()

b = int(b)
a = list(a)

answer = -1

check = [False] * len(a)
def getSolve(cnt, cur):
    global answer
    global check
    
    if cnt == len(a):
        if cur[0] == "0": return 
        cur = int(cur)
        if cur<b:
            answer = max(answer, cur)

        return 

    for i in range(len(a)):
        if not check[i]: 
            check[i] = True
            getSolve(cnt+1, cur+a[i])
            check[i] = False
    





for i in range(len(a)):
    check[i] = True
    getSolve(1, a[i])
    check[i] = False

print(answer)

