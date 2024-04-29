import copy
n = int(input())

max_number = []
min_number = []

for i in range(n):
    number = list(map(int,input().split()))
    if i==0:
        max_number = copy.deepcopy(number)
        min_number = copy.deepcopy(number)
    else:
        new_number = copy.deepcopy(number)
        

        new_number[0] = number[0] + max(max_number[0], max_number[1])
        new_number[1] = number[1] + max(max_number)
        new_number[2] = number[2] + max(max_number[1], max_number[2])

        max_number = copy.deepcopy(new_number)

         
        new_number = copy.deepcopy(number)
        new_number[0] = number[0] + min(min_number[0], min_number[1])
        new_number[1] = number[1] + min(min_number)
        new_number[2] = number[2] + min(min_number[1], min_number[2])

        min_number = copy.deepcopy(new_number)
        




print(max(max_number), min(min_number))