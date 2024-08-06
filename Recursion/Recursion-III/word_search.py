class Solution:
    def searchWord(self,index,row,col,board,word):
        if(index==len(word)):return True
        if(row==len(board) or row<0 or 
        col==len(board[0]) or col<0 or
        board[row][col]=='#' or 
        board[row][col]!=word[index]):return False
        
            
        temp = board[row][col]
        board[row][col] = '#'

        if(self.searchWord(index+1,row+1,col,board,word) or 
        self.searchWord(index+1,row-1,col,board,word) or
        self.searchWord(index+1,row,col+1,board,word) or
        self.searchWord(index+1,row,col-1,board,word)):return True
        
        board[row][col] = temp
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        index = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col]==word[index]):
                    if(self.searchWord(index,row,col,board,word)):
                        return True
        return False


# time complexity: O(4^k * m*n)  
# space complexity: O(k)(stack space) 
board = []
m,n = list(map(int,input().strip().split()))
board = [list(input().strip()) for i in range(m)]
print(board)
word = input().strip()
print(Solution().exist(board,word))



