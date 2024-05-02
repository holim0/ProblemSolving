n, m = map(int, input().split())


mapp = {}

group_mapping = {}

for _ in range(n):
    group_name = input()
    number = int(input())
    cur_name = []

    for _ in range(number):
        name = input()
        group_mapping[name] = group_name
        cur_name.append(name)
    
    cur_name = sorted(cur_name)

    mapp[group_name] = cur_name

for _ in range(m):
    name = input()
    order = int(input())

    if order == 0:
        for cur in mapp[name]:
            print(cur)
    else:
        print(group_mapping[name])

