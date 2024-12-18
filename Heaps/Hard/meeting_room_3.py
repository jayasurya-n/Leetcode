from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meetings_cnt = [0]*n
        rooms = list(range(n))
        ends = []
        heapq.heapify(rooms)
        
        for s,e in meetings:
            while(ends and s>=ends[0][0]):
                _,room = heapq.heappop(ends)
                heapq.heappush(rooms,room)
            
            if(rooms):    
                room = heapq.heappop(rooms)
                heapq.heappush(ends,(e,room))
                meetings_cnt[room]+=1
            
            else:
                end_time,room = heapq.heappop(ends)
                heapq.heappush(ends,(e-s+end_time,room))
                meetings_cnt[room]+=1
            
        return meetings_cnt.index(max(meetings_cnt))
                
# time complexity: O(mlogm+mlogn)
# space complexity: O(m+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))