n, game = input().split()

nameSet = set()

for _ in range(int(n)):
    name = input()
    nameSet.add(name)


if game == "Y":
    print(len(nameSet))

elif game == "F":
    cnt = (len(nameSet))//2
    print(cnt)
else:
    cnt = len(nameSet)//3
    print(cnt)