t = int(input())

for _ in range(t):
    n = int(input())

    price = list(map(int, input().split()))
    stack = []
    answer = 0
    max_value = price[-1]
    for i in range(len(price)-2, -1, -1):
        max_value = max(max_value, price[i])

        if max_value>price[i]:
            answer+= (max_value-price[i])       
        

    print(answer)