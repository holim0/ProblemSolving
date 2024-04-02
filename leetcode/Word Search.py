class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = len(board[0])
        h = len(board)


        def find(idx, i, j, visited):
            if idx == len(word)-1:
                return True

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i+x, j+y

                if 0<=ni<h and 0<=nj<w:
                    if not visited[ni][nj] and word[idx+1] == board[ni][nj]:
                        visited[ni][nj] = True
                        if find(idx+1, ni, nj, visited): return True
                        visited[ni][nj] = False
            

        for i in range(h):
            for j in range(w):
                visited = [[False for _ in range(w)] for _ in range(h)]
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if find(0, i, j, visited): return True

                    visited[i][j] = False
        
        return False


        