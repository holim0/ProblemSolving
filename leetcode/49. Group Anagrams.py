class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anaMap = {}

        for s in strs:
            cur = sorted(s)
            cur = "".join(cur)
            
            if cur not in anaMap:
                anaMap[cur] = [s]
            else:
                anaMap[cur].append(s)
        
        for key in anaMap:
            answer.append(anaMap[key])
        
        return answer