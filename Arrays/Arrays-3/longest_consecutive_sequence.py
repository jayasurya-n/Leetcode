class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        hash  = set()
        for i in range(n):
            hash.add(nums[i])

        ans = 1
        for val in hash:
            if ((val-1) in hash):continue
            cnt = 1
            temp = val
            while((temp+1) in hash):
                cnt+=1
                temp+=1
            ans = max(ans,cnt)
        return ans
                        
        

nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.longestConsecutive(nums))


