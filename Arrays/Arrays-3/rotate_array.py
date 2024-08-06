class Solution:

    def reverse(self,nums,start,end):
        while(start<end):
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First Solution
        # arr = [0 for i in range(n)]
        # for i in range(n):
        #     index = (i+k)%n
        #     arr[index] = nums[i]

        # for i in range(n):
        #     nums[i] = arr[i]

        # Second Solution
        # n  = len(nums)
        # k = k%n
        # temp =  [nums[i] for i in range(n-k)]

        # for i in range(n-k,n):
        #     nums[i-(n-k)] = nums[i]
        
        # print(nums)
        # for i in range(k,n):
        #     nums[i] = temp[i-k]

        # # Third Solution
        # n  = len(nums)
        # k = k%n
        # nums[:] = nums[-k:] + nums[:-k]

        # Fourth Solution
        n = len(nums)
        k = k%n
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)

        return nums
        
 

k = int(input())
nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.rotate(nums,k))