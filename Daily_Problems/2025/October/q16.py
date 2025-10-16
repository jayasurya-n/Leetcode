import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def findSmallestInteger(self, nums, value: int) -> int:
        freq = [0]*value
        for num in nums:
            freq[num%value]+=1
        
        ans = 0
        while True:
            for i in range(value):
                if(freq[i]==0):return ans+i
                freq[i]-=1
            ans+=value

# time complexity: O(n+value)
# space complexity: O(value)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)