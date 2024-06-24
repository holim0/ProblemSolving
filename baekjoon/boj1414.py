import sys
sys.setrecursionlimit(1000)
n = int(input())

answer = 0
def getAlphaValue(cur):

    value = ord(cur)-96

    if value<0:
        value+=58
    return value

link = []
parent = [i for i in range(n)]
for i in range(n):
    row = input()
    row = list(row)
    for j in range(n):
        if row[j] != "0":
            answer+=getAlphaValue(row[j])
            link.append((getAlphaValue(row[j]), i, j))


link.sort()

def merge(a, b):

    a = find(a)
    b = find(b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a

    return find(parent[a])

linkCnt = 0
for dist, a, b in link:
    if find(a) != find(b):
        merge(a, b)
        answer-=dist
        linkCnt+=1


if linkCnt==n-1:
    print(answer)
else:
    print(-1)
