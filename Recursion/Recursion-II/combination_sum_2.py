class Solution:
    def findCombinations(self,start,arr,stored,ans,target):
        if(target==0):
            ans.append(stored[:])
            return
    
        for i in range(start,len(arr)):
            if(i>start and arr[i]==arr[i-1]):continue
            if(arr[i]>target):break

            stored.append(arr[i])
            self.findCombinations(i+1,arr,stored,ans,target-arr[i])
            stored.pop()
        
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        start = 0
        stored = []
        candidates.sort()
        self.findCombinations(start,candidates,stored,ans,target)
        return ans

# time complexity: O((2^n)*k), k=average space for store
# space complexity: O(n)(recursion stack)
arr = list(map(int,input().strip().split()))
target = int(input().strip()) 
print(Solution().combinationSum2(arr,target))