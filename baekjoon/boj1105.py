import sys
l, r = map(int, input().split())

sl = str(l)
sr = str(r)

if len(sl) != len(sr):
    print(0)
    sys.exit()

cnt = 0
for i in range(len(sl)):
    if sl[i] == sr[i]:
        if sl[i] == "8":
            cnt+=1
    else:
        break

print(cnt)


 
