from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class ProductOfNumbers:
    def __init__(self):
        self.ppro = [1]

    def add(self, num: int) -> None:
        if(num==0):self.ppro = [1]
        else:self.ppro.append(self.ppro[-1]*num)

    def getProduct(self, k: int) -> int:
        n = len(self.ppro)-1
        if(n<k):return 0
        return self.ppro[n]//self.ppro[n-k]

# time complexity: O(1),O(1)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))