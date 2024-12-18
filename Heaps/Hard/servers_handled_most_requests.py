from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = SortedList(range(k))
        requests = [0]*k
        busy = []
        
        for i,t in enumerate(arrival):
            while busy and busy[0][0]<=t:
                _,fs = heapq.heappop(busy)
                servers.add(fs)
                
            if(not servers):continue
            
            pos = bisect.bisect_left(servers,i%k)
            if(pos==len(servers)):pos = 0
            assigned = servers.pop(pos)
            requests[assigned]+=1
            heapq.heappush(busy,(t+load[i],assigned))
        
        maxi = max(requests)
        return [i for i,cnt in enumerate(requests) if cnt==maxi]

# time complexity: O(nlogk)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))