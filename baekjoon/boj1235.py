n = int(input())


number = []

for _ in range(n):
    num = input()
    number.append(num)

numSize = len(number[0])

mapp = {}
for i in range(1, numSize+1):
    isAnswer = True
    for n in number:
        cur = n[numSize-i:numSize]
        if cur not in mapp:
            mapp[cur] = True
        else:
            isAnswer = False
            break
    
    if isAnswer:
        print(i)
        break