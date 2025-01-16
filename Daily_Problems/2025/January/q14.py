from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash1 = set()
        hash2 = set()
        
        ans = []
        cnt = 0
        for i in range(len(A)):
            hash1.add(A[i])
            hash2.add(B[i])
            
            if(A[i]==B[i]):cnt+=1
            else:
                if(A[i] in hash2):cnt+=1
                if(B[i] in hash1):cnt+=1
            ans.append(cnt)
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))