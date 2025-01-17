from typing import List,Optional
import sys
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        
        freq = dict(sorted(freq.items(),key=lambda x:(x[1],-x[0])))

        nums = []
        for key,val in freq.items():
            for cnt in range(val):
                nums.append(key)
        return nums


# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        print(Solution().frequencySort(nums))