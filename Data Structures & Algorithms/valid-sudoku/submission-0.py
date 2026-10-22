class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        if not m or not n or m != n:
            return False
        
        row = [set() for _ in range(m)]
        col = [set() for _ in range(m)]
        ret = [[set() for _ in range(m)] for _ in range(m)]

        for i in range(m):
            for j in range(m):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in ret[i//3][j//3]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    ret[i//3][j//3].add(board[i][j])
        return True