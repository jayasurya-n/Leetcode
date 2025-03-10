from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def JobSequencing(self, id, deadline, profit):
        n = len(profit)
        profit_index = [(p,i) for i,p in enumerate(profit)]
        profit_index.sort(reverse=True)
        
        days = [False]*(max(deadline)+1)
        
        ans = jobs = 0
        for i in range(n):
            p,ind = profit_index[i]
            cur_deadline = deadline[ind]
            for j in range(cur_deadline,0,-1):
                if(days[j]==False):
                    days[j] = True
                    jobs+=1
                    ans+=p
                    break
        return [jobs,ans]
                    
# time complexity: O(nlogn+n*deadlines)
# space complexity: O(n+deadlines)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))