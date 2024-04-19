n, s = map(int, input().split())

number = list(map(int, input().split()))

answer = 0

def find(sum, idx):
    global answer
    global number
    if sum==s:
        answer+=1
    
    if idx==n-1:
        return
    

    for i in range(idx+1, n):
        find(sum+number[i], i)

    
        

for i in range(n):
    find(number[i], i)

print(answer)