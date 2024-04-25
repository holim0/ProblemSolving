s, e, q = input().split()

isIn = {}
isOut = {}

sh, sm = map(int, s.split(":"))
sStamp = 60 * sh + sm
eh, em = map(int, e.split(":"))
eStamp = 60 * eh + em
qh, qm = map(int, q.split(":"))
qStamp = 60 * qh + qm

answer = 0

while True:
    try:
        time, name = input().split()

        curH, curM = map(int, time.split(":"))
        curStamp = 60 * curH + curM

        if curStamp<=sStamp:
            isIn[name] = name
        
        elif eStamp<=curStamp<=qStamp:
            if name in isIn and name not in isOut:
                isOut[name] = name


    except:
        break
    

print(len(isOut))