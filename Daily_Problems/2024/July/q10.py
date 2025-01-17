from typing import List,Optional
import sys
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        print(logs)
        for i in range(len(logs)):
            if(logs[i]=='./'):continue
            elif(logs[i]=='../'):
                if(level>0):level-=1
            else:level+=1
        return level





# time complexity: O(n)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        logs = input().strip().split(',')
        print(Solution().minOperations(logs))