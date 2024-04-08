class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s, e = 0, len(nums)-1
        if len(nums)==1: return 0

        while s<=e:

            mid = (s+e)//2
            
            if mid ==0:
                if nums[mid] > nums[mid+1]:
                    return 0
                else:
                    s = mid+1
                
                continue


            if mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    e = mid-1
                continue

            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid-1] > nums[mid]:
                e = mid-1
                continue
            
            if nums[mid+1] > nums[mid]:
                s = mid+1
                continue
        