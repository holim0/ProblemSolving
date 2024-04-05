class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        jump = 0

        max_jump_idx = 0 # 현재 위치에서 최대로 갈 수 있는 곳

        lastJumpIdx = 0 # 이전 최대 갈 수 있는 idx (이 곳을 벗어나면 점프한 것 )

        for i in range(len(nums)):
            max_jump_idx = max(max_jump_idx, i + nums[i])

            if i == lastJumpIdx: # 이전 범위를 벗어났음.
                lastJumpIdx = max_jump_idx
                jump+=1

                if max_jump_idx >= len(nums)-1: return jump

        
        return jump