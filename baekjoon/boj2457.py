import sys
n = int(input())
answer = 0
flower = []

daylist = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



def getTotalDay(month, day):
    curDay = 0
    for i in range(0, month):
        curDay+=daylist[i]
    
    curDay+=day

    return curDay

likeStart, likeEnd = getTotalDay(3, 1), getTotalDay(11, 30)
for _ in range(n):
    a, b, c, d = map(int, input().split())
    flower.append((getTotalDay(a, b),getTotalDay(c, d)))


flower.sort()


curEndDate = likeStart


def getNext():
    global curEndDate
    global answer
    nxtEndDate = -1
    newflower = []
    
    for i in range(len(flower)):
        s, e = flower[i]
        if s<=curEndDate:
            nxtEndDate = max(nxtEndDate, e)
        else:
            newflower.append((s, e))

    
    curEndDate = nxtEndDate
    answer+=1
    return newflower

while len(flower):

    if curEndDate>likeEnd or curEndDate ==-1:
        break
    
    flower = getNext()
    

if curEndDate>likeEnd:
    print(answer)
else:
    print(0)

