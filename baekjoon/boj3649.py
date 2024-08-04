while True:

    try:
        x = int(input())
        n = int(input())
        x = x* pow(10, 7)
        lego =[]

        for _ in range(n):
            l = int(input())
            lego.append(l)

        lego.sort()

        s, e = 0, len(lego)-1
        isBreak = False
        while s<e:

            curSum = lego[s] + lego[e]

            if curSum>x:
                e-=1
            elif curSum<x:
                s+=1
            
            elif curSum==x:
                print("yes", lego[s], lego[e])
                isBreak = True
                break
        
        if not isBreak:
            print("danger")


    except:
        break