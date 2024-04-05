# dp로 구현시 느림
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        INF = 1e10

        dp = [INF for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            step = nums[i]
            
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]