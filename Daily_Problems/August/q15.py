from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives,tens = 0,0
        for i in range(len(bills)):
            if(bills[i]==5):fives+=1
            elif(bills[i]==10):
                tens+=1
                if(fives==0):return False
                fives-=1
            else:
                if(tens>=1 and fives>=1):
                    tens-=1
                    fives-=1
                elif(tens==0 and fives>=3):fives-=3
                else:return False
        return True


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))