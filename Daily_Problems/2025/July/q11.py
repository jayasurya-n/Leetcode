from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0]*n
        rooms_pq = list(range(0,n))
        heapq.heapify(rooms_pq)
        ends_pq = []

        for start,end in meetings:
            duration = end-start
            while ends_pq and ends_pq[0][0]<=start:
                _,room_num = heapq.heappop(ends_pq)
                heapq.heappush(rooms_pq,room_num)

            if rooms_pq:
                room_num = heapq.heappop(rooms_pq)
                count[room_num]+=1
                heapq.heappush(ends_pq,(end,room_num))
            
            else:
                end_time,room_num = heapq.heappop(ends_pq)
                count[room_num]+=1
                heapq.heappush(ends_pq,(end_time+duration,room_num))
        
        return count.index(max(count))

# time complexity: O(mlogm+mlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))