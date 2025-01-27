from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        num_to_group = defaultdict(int)
        groups = defaultdict(deque)
        sorted_nums = sorted(nums)
        
        group_number = 1
        num_to_group[sorted_nums[0]] = group_number
        groups[group_number].append(sorted_nums[0])
        
        for i in range(n-1):
            if(sorted_nums[i+1]-sorted_nums[i]>limit):group_number+=1
            num_to_group[sorted_nums[i+1]] = group_number
            groups[group_number].append(sorted_nums[i+1])
        
        for i in range(n):
            group_number = num_to_group[nums[i]]
            nums[i] = groups[group_number].popleft()
        return nums

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))