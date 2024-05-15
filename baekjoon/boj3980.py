from itertools import permutations as permu
c = int(input())

answer = 0

order = []
check = [False for _ in range(11)]
mapp = []
def find(depth, positionNumber, ability):
    global answer
    global check
    if depth == 10:
        answer = max(answer, ability)
        return 
    
    for i in range(11):
        if not check[i] and mapp[i][positionNumber+1] !=0:
            check[i] = True
            find(depth+1, positionNumber+1, ability+mapp[i][positionNumber+1])
            check[i] = False
        
    

for _ in range(c):
    mapp = []
    check = [False for _ in range(11)]
    answer = 0
    for _ in range(11):
        row = list(map(int, input().split()))
        mapp.append(row)

    for i in range(11):
        if mapp[i][0] !=0:
            check[i] = True
            find(0, 0, mapp[i][0])
            check[i] = False
    
    print(answer)
