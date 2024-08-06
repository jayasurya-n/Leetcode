class Solution:
    def findCombinations(self,index,arr,stored,ans,target):
        if(index==len(arr)):
            if(target==0):ans.append(stored[:])
            return

        if(arr[index]<=target):
            stored.append(arr[index])
            self.findCombinations(index,arr,stored,ans,target-arr[index])
            stored.pop()

        self.findCombinations(index+1,arr,stored,ans,target)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        index = 0
        stored = []
        self.findCombinations(index,candidates,stored,ans,target)
        return ans

# time complexity: O((2^target)*k), because if only 1 is there then we need to recurse target times 
# and k=average space for store
# space complexity: O(n)(recursion stack)
arr = list(map(int,input().strip().split()))
target = int(input().strip()) 
print(Solution().combinationSum(arr,target))