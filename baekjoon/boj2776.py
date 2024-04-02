import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    s1 = []

    value = map(int, input().split())

    s1 = list(value)

    m = int(sys.stdin.readline())

    value = map(int, input().split())

    s2 = list(value)

    answer = []
    s1 = sorted(s1)

    for v in s2:
        s, e = 0, len(s1)-1
        isbreak = False
        while s<=e:
            mid = (s+e)//2
            if s1[mid] == v:
                print(1)
                isbreak = True
                break

            if s1[mid] < v:
                s = mid+1

            else:
                e = mid -1
        
        if not isbreak:
            print(0)
        
        isbreak = False
        


