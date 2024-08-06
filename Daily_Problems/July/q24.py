from typing import List,Optional
import sys
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hash = []
        for i in range(len(nums)):
            number = str(nums[i])
            s = ""
            for j in range(len(number)):
                new_digit = str(mapping[int(number[j])])
                s+=new_digit
            
            hash.append((int(s),i))
        
        hash.sort()
        ans = []
        for pair in hash:
            ans.append(nums[pair[1]])
        return ans

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        mapping = list(map(int,input().strip().split()))
        nums = list(map(int,input().strip().split()))
        print(Solution().sortJumbled(mapping,nums))