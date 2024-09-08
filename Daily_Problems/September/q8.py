from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        len = 0
        while(temp):
            len+=1
            temp = temp.next
        
        q = len//k
        r = len%k
        
        ans = [None for _ in range(k)]
        
        temp = head
        prev = None
        ind = 0
        while(temp):
            ans[ind] = temp
            q1 = q+1 if r>0 else q
            for i in range(q1):
                prev = temp
                temp = temp.next
            prev.next = None
            ind+=1
            r-=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))