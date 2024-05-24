n = int(input())

word = []

for _ in range(n):
    w = input()
    word.append(w)

target = {}

for w in word[0]:
    if w not in target:
        target[w] = 1
    else:
        target[w]+=1

answer = 0

firstWord = list(word[0])
firstWord = sorted(firstWord)
firstWord = "".join(firstWord)

for i in range(1, n):
    target = list(firstWord)[:]

    cnt = 0

    curWord = word[i]

    for w in curWord:
        if w in target:
            target.remove(w)
        else:
            cnt+=1

    if cnt < 2 and len(target) <2:
        answer+=1

print(answer)