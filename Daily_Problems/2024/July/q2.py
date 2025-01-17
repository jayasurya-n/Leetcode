from typing import List
import sys
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums1)>len(nums2)):return self.intersect(nums2,nums1)
        nums1.sort()
        nums2.sort()
        i,j,k=0,0,0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]==nums2[j]):
                nums2[k]=nums1[i]
                i+=1;j+=1;k+=1
            elif(nums1[i]<nums2[j]):i+=1
            else:j+=1
        return nums2[:k]


# time complexity: O(nlogn+mlogm) 
# space complexity: O(1)

if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums1 = list(map(int,input().strip().split()))
        nums2 = list(map(int,input().strip().split()))
        print(Solution().intersect(nums1,nums2))