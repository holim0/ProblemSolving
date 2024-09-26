# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        q = []

        for curList in lists:
            while curList:
                hp.heappush(q, curList.val)
                curList = curList.next
        if len(q) ==0: return None
        answer = ListNode()
        curNode = answer
        while q:
            cur = hp.heappop(q)
            
            curNode.val = cur
            if len(q) ==0: break
            curNode.next = ListNode()
            curNode = curNode.next
        
        return answer
