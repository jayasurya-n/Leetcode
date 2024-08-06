class Solution:
    # def isSafe(self,row,col,board,n):
    #     drow,dcol = row,col

    #     while(drow>=0 and dcol>=0):
    #         if(board[drow][dcol]=='Q'):return False
    #         drow-=1
    #         dcol-=1
        
    #     dcol = col
    #     while(dcol>=0):
    #         if(board[row][dcol]=='Q'):return False
    #         dcol-=1
        
    #     while(row<n and col>=0):
    #         if(board[row][col]=='Q'):return False
    #         row+=1
    #         col-=1
        
    #     return True

    # def placeNQueens(self,col,board,ans,n):
    #     if(col==n):
    #         ans.append(["".join(row) for row in board])
    #         return
        
    #     for row in range(0,n):
    #         if(self.isSafe(row,col,board,n)):
    #             board[row][col] = 'Q'
    #             self.placeNQueens(col+1,board,ans,n)
    #             board[row][col] = '.'

    def placeNQueens(self,col,board,ans,n,leftRow,lowerDiag,upperDiag):
        if(col==n):
            ans.append(["".join(row) for row in board])
            return
        
        for row in range(0,n):
            if(leftRow[row]==0 and lowerDiag[row+col]==0 and upperDiag[n-1 +col-row]==0):
                leftRow[row]=1
                lowerDiag[row+col]=1
                upperDiag[n-1 + col-row]=1
                board[row][col] = 'Q'
                self.placeNQueens(col+1,board,ans,n,leftRow,lowerDiag,upperDiag)
                board[row][col] = '.'
                leftRow[row]=0
                lowerDiag[row+col]=0
                upperDiag[n-1 + col-row]=0

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [['.']*n for i in range(n)]
        leftRow = [0]*n
        lowerDiag = [0]*(2*n-1)
        upperDiag = [0]*(2*n-1)
        col = 0
        self.placeNQueens(col,board,ans,n,leftRow,lowerDiag,upperDiag)
        return ans



# time complexity: O(n!*n) or O(n!) for optimal  
# space complexity: O(n^2)+O(n)(stack space) , O(n^2)+O(n)+O(n)(stack space) for optimal
n = int(input())
print(Solution().solveNQueens(n))