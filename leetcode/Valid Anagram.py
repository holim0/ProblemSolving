class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t): return False
        for value in s:
            if value not in s_dict:
                s_dict[value] = 1
            else:
                s_dict[value]+=1
        
        for value in t:
            if value not in t_dict:
                t_dict[value] = 1
            else:
                t_dict[value]+=1

        for value in s:
            if value not in t_dict: return False
            if s_dict[value] != t_dict[value]:
                return False
        
        return True