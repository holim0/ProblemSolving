n = int(input())

dict = {}
answer = []
for _ in range(n):
    word = list(input().split())
    isDone = False
    for i in range(len(word)):
        w = word[i]
        if w[0].lower() not in dict:
            dict[w[0].lower()] = True
            new_w = "[" + w[0] + "]" + w[1:]
            word[i] = new_w
            isDone = True
            break 

    if not isDone:
        for k in range(len(word)):
            w = word[k]
            if isDone: break
            for i in range(len(w)):
                if w[i].lower() not in dict:
                    dict[w[i].lower()] = True
                    new_w = w[:i]+ "[" + w[i] + "]" + w[i+1:]
                    word[k] = new_w
                    isDone = True
                    break

    answer.append(" ".join(word))

for a in answer:
    print(a)