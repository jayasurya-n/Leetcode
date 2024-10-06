from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        deque1 = deque(sentence1.split())
        deque2 = deque(sentence2.split())

        while deque1 and deque2 and deque1[0]==deque2[0]:
            deque1.popleft()
            deque2.popleft()
        
        while deque1 and deque2 and deque1[-1]==deque2[-1]:
            deque1.pop()
            deque2.pop()
        
        return not deque1 or not deque2
        
        
# time complexity: O(l1+l2)
# space complexity: O(l1+l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))