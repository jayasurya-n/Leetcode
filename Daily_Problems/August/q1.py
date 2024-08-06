from typing import List,Optional
from collections import deque
import sys
class Solution:
    def countSeniors(self, details: List[str]):
        # ans = 0
        # for i in range(len(details)):
        #     if(int(details[i][-4:-2])>60):ans+=1
        # return ans
        return sum(int(x[-4:-2])>60 for x in details)


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))