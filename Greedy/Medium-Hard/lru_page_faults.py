from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def pageFaults(self, n, c, pages):
        cache = dict()
        time = 0
        page_faults = 0
        for page in pages:
            if(page not in cache):
                cache[page] = time
                page_faults+=1
            else:cache[page] = time
            
            if(len(cache)>c):
                min_page, min_time = 1001,n+1
                for page,time in cache.items():
                    if(min_time>time):
                        min_page = page
                        min_time = time
                cache.pop(min_page)
            time+=1
        return page_faults

# time complexity: O(nc)
# space complexity: O(c)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))