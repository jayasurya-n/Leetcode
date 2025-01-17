from typing import List,Optional
from collections import deque
import sys
class Solution:
    # def minHeightShelves(self, books: List[List[int]], shelfWidth: int):
    #     def solve(index,w,h,dp): 
    #         if(index==n):
    #             return h

    #         if(dp[index][w]!=-1):return dp[index][w] 

    #         curw = books[index][0] 
    #         curh = books[index][1]

    #         if(index==0):
    #             dp[index][w] = solve(index+1,curw,curh,dp)
    #             return dp[index][w]

    #         h1 = sys.maxsize
    #         if(w+curw<=shelfWidth):
    #             h1 = solve(index+1,w+curw,max(h,curh),dp)
            
    #         h2 = h+solve(index+1,curw,curh,dp)
    #         dp[index][w] = min(h1,h2)
    #         return dp[index][w]
        
    #     n = len(books)
    #     dp = [[-1]*(shelfWidth+1) for _ in range(n)]
    #     return solve(0,0,0,dp)

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int):
        
        n = len(books)
        dp = [[sys.maxsize]*(shelfWidth+1) for _ in range(n)]
        for w in range(shelfWidth+1):
            if(books[0][0]<=w):dp[0][w] = books[0][1]    

        for i in range(1,n):
            curw = books[i][0]
            curh = books[i][1]
            for w in range(1,shelfWidth+1):
                if(curw<=w):
                    dp[i][w] = max(dp[i-1][w-curw],curh)
                
                dp[i][w] = min(dp[i][w],curh+dp[i-1][0])
        
        return dp[n-1][shelfWidth]



# time complexity: O(n*w)
# space complexity: O(n*w)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,shelfWidth = list(map(int,input().strip().split()))
        books = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().minHeightShelves(books,shelfWidth))

