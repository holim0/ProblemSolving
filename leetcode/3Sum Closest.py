class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        diff = 1e10
        answer = 0

        for i in range(len(nums)):
            f_value = nums[i]

            p1, p2 = i+1, len(nums)-1
            curTarget = target - f_value
            while p1<p2:
                v1, v2 = nums[p1], nums[p2]
                s = v1+v2

                if abs(curTarget-s)<diff:
                    diff = abs(curTarget-s)
                    answer = s + f_value

                if curTarget > s:
                    p1+=1
                elif curTarget <s:
                    p2-=1
                else:
                    return target

        return answer
        