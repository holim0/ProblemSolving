class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer =[]
        m = len(heights[0])
        n = len(heights)
        
        p_land = set()
        a_land = set()
    
        def getSol(cx, cy, land):
            
            land.add((cx, cy))

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b
                
                if 0<=nx<n and 0<=ny<m:
                    if heights[cx][cy]<=heights[nx][ny] and (nx, ny) not in land:
                        getSol(nx, ny, land)
        


        for i in range(0, m):
            x, y = 0, i
            getSol(x, y, p_land)
        
        for i in range(0, n):
            x, y = i, 0
            getSol(x, y, p_land)
        
        for i in range(0, n):
            x, y = i, m-1
            getSol(x, y, a_land)

        for i in range(0, m):
            x, y = n-1, i
            getSol(x, y, a_land)

        answer = list(p_land & a_land)
        
        return answer