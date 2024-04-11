import sys
import math
input  = sys.stdin.readline

n = int(input())

number = list(map(int, input().split()))

o = list(map(int, input().split()))
LIMIT = math.pow(10, 10)

plus, minus, mul, div = o[0], o[1], o[2], o[3]
max_answer, min_answer = (-1) * LIMIT, LIMIT

def cal(curValue, curIdx, cur_o):
    global max_answer
    global min_answer
    
    if curIdx == n-1:
        
        max_answer = max(max_answer, curValue)
        min_answer = min(min_answer, curValue)
        return


    pl, mi, mu, di = cur_o

    if pl>0:
        cal(curValue+number[curIdx+1], curIdx+1, (pl-1, mi, mu, di))
    if mi>0:
        cal(curValue-number[curIdx+1], curIdx+1, (pl, mi-1, mu, di))

    if mu>0:
        cal(curValue*number[curIdx+1], curIdx+1, (pl, mi, mu-1, di))

    if di>0:
        nxt_Value = 0
        if curValue <0:
            nxt_Value = (-1 * curValue) // number[curIdx+1]
            nxt_Value *= (-1)
        else:
            nxt_Value = (curValue) // number[curIdx+1]
        cal(nxt_Value, curIdx+1, (pl, mi, mu, di-1))



cal(number[0], 0, (plus, minus, mul, div))



print(max_answer)
print(min_answer)