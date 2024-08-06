from typing import List,Optional
from collections import deque
import sys
class Solution:
    def asteroidCollision(self, asteroids: List[int]):
        stack = []
        for i in range(len(asteroids)):
            if(stack==[] or 
                (stack[-1]>0 and asteroids[i]>0) or 
                (stack[-1]<0 and asteroids[i]<0) or
                (stack[-1]<0 and asteroids[i]>0)):stack.append(asteroids[i])
            else:
                while(stack and stack[-1]>0 and stack[-1]<abs(asteroids[i])):stack.pop()
                if(stack==[] or stack[-1]<0):stack.append(asteroids[i])
                elif(stack[-1]==abs(asteroids[i])):stack.pop()
        return stack

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        asteroids = list(map(int,input().strip().split()))
        print(Solution().asteroidCollision(asteroids))