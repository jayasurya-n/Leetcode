from typing import List
class Solution:
    def findMinimumCoins(self,coins,V) -> int:
        ans = []
        i = len(coins)-1
        while(V!=0):
            while(i>=0 and coins[i]>V):i-=1
            if(i<0):ans.append(-1);break
            V-=coins[i]
            ans.append(coins[i])
        return ans
       
        
            
# This algorithm only works in specific test cases,otherwise we need to use DP
# time complexity: O(V) 
# space complexity: O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        # 2 3 10 20 50 100 500 1000
        coins = list(map(int,input().strip().split()))
        V = int(input().strip())
        print(Solution().findMinimumCoins(coins,V))