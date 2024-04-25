n = int(input())

word = []

for _ in range(n):
    w = input()
    word.append(w)

answer = 0

for i in range(n):
    for j in range(i+1, n):
        dict = {}
        w1, w2, size = word[i], word[j], len(word[i])
        isSame = True
        for k in range(size):
            if w1[k] not in dict:
                dict[w1[k]] = w2[k]
            else:
                if dict[w1[k]] != w2[k]:
                    isSame = False
                    break
            

        if not isSame: continue

        dict ={}
        for k in range(size):
            if w2[k] not in dict:
                dict[w2[k]] = w1[k]
            else:
                if dict[w2[k]] != w1[k]:
                    isSame = False
                    break
        if isSame:
            answer+=1

print(answer)