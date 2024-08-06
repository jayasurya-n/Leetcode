from typing import List,Optional
from collections import deque
import sys
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]):
        freq1,freq2 = dict(),dict()
        for i in range(len(target)):
            freq1[arr[i]] = freq1.get(arr[i],0)+1 
            freq2[target[i]] = freq2.get(target[i],0)+1 
        
        for key,val1 in freq1.items():
            val2 = freq2.get(key,0)
            if(val2!=val1):return False
        return True
            


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))