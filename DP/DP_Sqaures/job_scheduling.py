from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def JobScheduling(self,jobs,n):
        jobs.sort(key = lambda job:job.profit, reverse=True)
        maxDeadline = max(job.deadline for job in jobs)
        time = [False]*(maxDeadline+1)
        
        cnt = 0
        maxProfit = 0
        for job in jobs:
            for t in range(job.deadline,0,-1):
                if(time[t]==False):
                    maxProfit+=job.profit
                    cnt+=1
                    time[t] = True
                    break
        return [cnt,maxProfit]
                
# time complexity: O(nlogn+n*maxDeadline)
# space complexity: O(maxDeadline)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))