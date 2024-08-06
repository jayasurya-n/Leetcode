class Solution:
    def findPaths(self,row,col,maze,store,ans):
        if(row == len(maze)-1 and col==len(maze)-1 and maze[row][col]==1):
            ans.append("".join(store))
            return
         
        if(row<0 or row>=len(maze) or
            col<0 or col>=len(maze) or
            maze[row][col]==0):return

        temp = maze[row][col] 
        maze[row][col] = 0 
        self.findPaths(row+1,col,maze,store+['D'],ans)
        self.findPaths(row-1,col,maze,store+['U'],ans)
        self.findPaths(row,col+1,maze,store+['R'],ans)
        self.findPaths(row,col-1,maze,store+['L'],ans)
        maze[row][col] = temp


    def findPath(self, maze, n):
        ans,store = [],[]
        row,col = 0,0
        self.findPaths(row,col,maze,store,ans)
        return ans

# time complexity: O(4^(m*n))  
# space complexity: O(m*n)(stack space) 
n = int(input().strip())
maze = [list(map(int,input().strip().split())) for _ in range(n)]
print(Solution().findPath(maze,n))




