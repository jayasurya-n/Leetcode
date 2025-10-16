import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def hasIncreasingSubarrays(self, nums, k: int) -> bool:
        n = len(nums)
        for i in range(n-2*k+1):
            ok = True
            for j in range(1,k):
                if(nums[i+j]<=nums[i+j-1]):
                    ok = False
                    break
            
            for j in range(k+1,2*k):
                if(nums[i+j]<=nums[i+j-1]):
                    ok = False
                    break
            
            if(ok):return True
        
        return False

# time complexity: O(n*k)
# space complexity: O(1)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        arr = lii()
        k = ii()
        ans = Solution().hasIncreasingSubarrays(arr,k)
        print(ans)