from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    #     ans = [[-1]*n for _ in range(m)]
    #     l,r = 0,n-1
    #     t,b = 0,m-1
    #     temp = head
    #     while(l<=r and t<=b):
    #         j = l
    #         while(j<=r and temp):
    #             ans[t][j] = temp.val
    #             temp = temp.next
    #             j+=1
    #         t+=1
            
    #         i = t
    #         while(i<=b and temp):
    #             ans[i][r] = temp.val
    #             temp = temp.next
    #             i+=1
    #         r-=1
            
    #         if(t<=b):
    #             j = r
    #             while(j>=l and temp):
    #                 ans[b][j] = temp.val
    #                 temp = temp.next
    #                 j-=1
    #             b-=1
            
    #         if(l<=r):
    #             i = b
    #             while(i>=t and temp):
    #                 ans[i][l] = temp.val
    #                 temp = temp.next
    #                 i-=1
    #             l+=1
                
    #     return ans
    
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        steps = [(0,1),(1,0),(0,-1),(-1,0)]
        dir = 0
        temp = head
        ans = [[-1]*n for _ in range(m)]
        i,j = 0,0
        while(temp):
            ans[i][j] = temp.val 
            ni=i+steps[dir][0]
            nj=j+steps[dir][1]
            
            if(ni>=m or ni<0 or 
               nj>=n or nj<0 or 
               ans[ni][nj]!=-1):
                dir = (dir+1)%4
            
            i+=steps[dir][0]
            j+=steps[dir][1]
            temp = temp.next
        return ans
            
# time complexity: O(mn),O(mn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))