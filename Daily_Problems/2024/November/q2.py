from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if(sentence[i]==" " and sentence[i-1]!=sentence[i+1]):return False
        return sentence[0]==sentence[-1]

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))