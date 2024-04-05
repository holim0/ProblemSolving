class Solution:
    def canJump(self, nums: List[int]) -> bool:


        cur_goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            step = nums[i]

            next_pos = i + step

            if next_pos >= cur_goal:
                cur_goal = i
        

        if cur_goal ==0: return True
        return False

            

        