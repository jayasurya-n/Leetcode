import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def maxIncreasingSubarrays(self, nums) -> int:
        n = len(nums)
        prev,curr,ans = 0,1,0
        for i in range(1,n):
            if(nums[i]>nums[i-1]):curr+=1
            else:
                ans = max(ans,curr//2,min(prev,curr))
                prev = curr
                curr = 1

        ans = max(ans,curr//2,min(prev,curr))
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)