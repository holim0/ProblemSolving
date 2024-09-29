class Solution:
    def maxArea(self, h: List[int]) -> int:
        answer = 0
        l, r = 0, len(h)-1

        while l<=r:
            curWidth = r-l
            leftValue = h[l]
            rightValue = h[r]
            curHeight = min(leftValue, rightValue)
            
            answer = max(answer, curWidth * curHeight)

            if leftValue > rightValue:
                r-=1
            elif leftValue < rightValue:
                l+=1
            else:
                r-=1
                l+=1
            
        return answer