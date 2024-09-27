from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq
from sortedcontainers import SortedDict

class MyCalendarTwo:
    
    # def __init__(self):
    #     self.single_bookings = []
    #     self.double_bookings = []
        
    # def book(self, start: int, end: int) -> bool:
    #     for s,e in self.double_bookings:
    #         if(start<e and s<end):return False
        
    #     for s,e in self.single_bookings:
    #         if(start<e and s<end):
    #             ns = max(start,s)
    #             ne = min(end,e)
    #             self.double_bookings.append([ns,ne])
        
    #     self.single_bookings.append([start,end])
    #     return True
    
    def __init__(self):
        self.bookings = SortedDict()
        self.maxBookings = 2
        
    def book(self, start: int, end: int) -> bool:
        self.bookings[start] = self.bookings.get(start,0)+1 
        self.bookings[end] = self.bookings.get(end,0)-1
        
        cnt = 0
        for val in self.bookings.values():
            cnt+=val
            if(cnt>self.maxBookings):
                self.bookings[start] = self.bookings.get(start,0)-1 
                self.bookings[end] = self.bookings.get(end,0)+1
                return False
        
        return True
             
# time complexity: O(n^2),O(n^2logn)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))