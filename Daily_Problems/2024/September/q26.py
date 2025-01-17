from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq
from sortedcontainers import SortedList

# class MyCalendar:
    
#     def __init__(self):
#         self.bookings = []
        
#     def book(self, start: int, end: int) -> bool:
#         for s,e in self.bookings:
#             if(start<e and end>s):return False
#         self.bookings.append([start,end])
#         return True

# # time complexity: O(n^2)
# # space complexity: O(n)

class MyCalendar:
    
    def __init__(self):
        self.bookings = SortedList()
        
    def book(self, start: int, end: int) -> bool:
        ind = self.bookings.bisect_left([start,end])
        if((ind>0 and self.bookings[ind-1][1]>start) or (ind<len(self.bookings) and self.bookings[ind][0]<end)):
            return False
        self.bookings.add([start,end])
        return True

# time complexity: O(nlogn)
# space complexity: O(n)

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))