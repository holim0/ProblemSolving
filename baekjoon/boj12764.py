import heapq
import sys
input = sys.stdin.readline
n = int(input())

time =[]

for _ in range(n):
    p, q = map(int, input().split())
    time.append((p, q))

visit_cnt = [0 for _ in range(n)]

time = sorted(time)
q = []
empty = []

visit_cnt[0] +=1
heapq.heappush(q, (time[0][1], 0))
for i in range(1, len(time)):
    s, e = time[i]
    
    while q:
        eariest_end, seat_number = heapq.heappop(q)
        if s<eariest_end:
            heapq.heappush(q, (eariest_end, seat_number))
            break
        
        heapq.heappush(empty, (seat_number, eariest_end))

    
    if len(empty) >0:
        seat_number, eariest_end = heapq.heappop(empty)
        visit_cnt[seat_number]+=1
        heapq.heappush(q, (e, seat_number))
    else:
        occu = len(q)
        visit_cnt[occu]+=1
        heapq.heappush(q, (e, occu))
        
        
            
        
answer = 0
answer_list = []

for v in visit_cnt:
    if v !=0:
        answer+=1
        answer_list.append(str(v))

print(answer)
print(" ".join(answer_list))

