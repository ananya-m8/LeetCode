class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows=len(board)
        col=len(board[0])
        q=deque()
        for i in range(rows):
            if board[i][0]=='O':
                q.append((i,0))  
            if board[i][col-1]=='O':
                q.append((i,col-1))
        for i in range(col):
            if board[0][i]=='O':
                q.append((0,i))
            if board[rows-1][i]=='O':
                q.append((rows-1,i))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            board[r][c]='#'
            for i,j in directions:
                nr,nc=r+i,c+j
                if 0<=nr<rows and 0<=nc<col and board[nr][nc]=='O':
                    q.append((nr,nc))
        for i in range(rows):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
