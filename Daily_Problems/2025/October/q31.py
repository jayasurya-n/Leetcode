import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def getSneakyNumbers(self, nums):
        # n = len(nums)-2
        # s = sum(nums)
        # ss = sum(x*x for x in nums)
        # s2 = s - (n*(n-1))//2
        # ss2 = ss - (n*(n-1)*(2*n-1))//6
        # x1 = (s2-math.sqrt(2*ss2-s2*s2))//2
        # x2 = (s2 + math.sqrt(2*ss2-s2*s2))//2
        # return [int(x1),int(x2)]

        n = len(nums)-2
        xor = 0
        for num in nums:xor^=num
        for i in range(n):xor^=i
        
        xor = xor&(-xor)
        x1 = x2 = 0

        for i in range(n):
            if(i&xor):x1^=i
            else:x2^=i
        
        for num in nums:
            if(num&xor):x1^=num
            else:x2^=num
        
        return [x1,x2]

# time complexity: O(1),O(1)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)