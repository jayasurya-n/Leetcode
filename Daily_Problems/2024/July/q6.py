from typing import List,Optional
import sys
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time%(2*(n-1))
        if(time<=n-1):
            return 1+time
        else:
            return n-(time-(n-1))





# time complexity: O(1)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,time = list(map(int,input().strip().split()))
        print(Solution().passThePillow(n,time))