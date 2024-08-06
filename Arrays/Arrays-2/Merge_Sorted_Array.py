class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while(j>=0):
            if(i>=0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        return nums1
        


        
m = int(input())
nums1 = [int(x) for x in input().strip().split()]

n = int(input())
nums2 = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.merge(nums1,m,nums2,n))