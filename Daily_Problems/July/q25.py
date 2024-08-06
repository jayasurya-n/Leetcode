from typing import List,Optional
from collections import deque
import sys
class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        lag = 5*(10**4)
        freq = [0]*(2*lag+1)

        for i in range(len(arr)):
            ele = arr[i]+lag
            freq[ele]+=1
        
        arr = []
        for i in range(len(freq)):
            if(freq[i]!=0):
                while(freq[i]>0):
                    arr.append(i-lag)
                    freq[i]-=1
        return arr


# time complexity: 
# space complexity: 
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().sortArray(arr))