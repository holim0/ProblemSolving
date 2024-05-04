import sys
input = sys.stdin.readline
cnt = {}

name = set()
size = 0

while True:

    
    namu = input().rstrip()
    if not namu: break
    size+=1
    name.add(namu)
    if namu not in cnt:
        cnt[namu] = 1
    else:
        cnt[namu]+=1

    

name = sorted(name)

for n in name:
    cur_cnt = cnt[n]
    rt = format(cur_cnt*100/size, ".4f")
    print(n, rt)
        


