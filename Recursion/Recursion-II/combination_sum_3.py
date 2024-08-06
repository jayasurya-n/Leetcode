class Solution:
    def findCombinations(self,index,cnt,sum,store,ans,k,n):
        if(cnt==k):
            if(sum==n):
                ans.append(store[:])
            return 

        for i in range(index,10):
            self.findCombinations(i+1,cnt+1,sum+i,store+[i],ans,k,n)
        
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        cnt,sum,index = 0,0,1
        ans,store = [],[]
        self.findCombinations(index,cnt,sum,store,ans,k,n)
        return ans

# time complexity: O(2^k)
# space complexity: O(k)(recursion stack)
t = int(input())
for i in range(t):
    k,n = list(map(int,input().strip().split()))
    print(Solution().combinationSum3(k,n))