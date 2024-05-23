t = int(input())


def isPanlin(cur):
    p1, p2 = 0, len(string)-1

    cnt = 0
    
    while p1<=p2:
        
        if cur[p1] != cur[p2]:
            if cur[p1+1] ==cur[p2]:
                pp1, pp2 = p1+1, p2
                isAnswer = True
                while pp1<=pp2:

                    if cur[pp1] != cur[pp2]:
                        isAnswer = False
                        break

                    pp1+=1
                    pp2-=1
                
                if isAnswer:
                    return "1"

            if cur[p1] == cur[p2-1]:
                p2-=1
                isAnswer = True
                while p1<=p2:

                    if cur[p1] != cur[p2]:
                        isAnswer = False
                        break

                    p1+=1
                    p2-=1
                
                if isAnswer:
                    return "1"
                
            return "2"
        else:
            p1+=1
            p2-=1
    
    
    return "0"

for _ in range(t):
    string = input()
    print(isPanlin(string))
