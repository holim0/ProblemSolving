class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1Len = len(nums1)
        num2Len = len(nums2)
        totalLen = num1Len + num2Len
        mid = totalLen//2
        curIdx = -1
        p1, p2 = 0, 0
        merge =[]
        while True:
            if curIdx==mid:
                if totalLen%2==0:
                    return (merge[curIdx-1] + merge[curIdx])/2
                else:
                    return merge[curIdx]


            if p1>=num1Len and p2>=num2Len: break
            if p1>=num1Len:
                merge.append(nums2[p2])
                p2+=1
                curIdx+=1
                continue
            if p2>=num2Len:
                merge.append(nums1[p1])
                p1+=1
                curIdx+=1
                continue


            if nums1[p1]<nums2[p2]:
                merge.append(nums1[p1])
                p1+=1
            
            else:
                merge.append(nums2[p2])
                p2+=1
            
            curIdx+=1
            
        
        
