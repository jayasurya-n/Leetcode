class Solution:

    def findMedianSortedArrays(self, arr1: list[int], arr2: list[int]) -> float:
        n1 = len(arr1)
        n2 = len(arr2)

        if(n1>n2):return self.findMedianSortedArrays(arr2,arr1)
        low = 0
        high = n1

        while(low<=high):
            mid1 = (low+high)//2
            mid2 = (n1+n2+1)//2 - mid1
            l1,l2 = -1e7,-1e7
            r1,r2 = 1e7,1e7
            if(mid1<n1):r1 = arr1[mid1]
            if(mid2<n2):r2 = arr2[mid2]
            if(mid1-1>=0):l1 = arr1[mid1-1]
            if(mid2-1>=0):l2 = arr2[mid2-1]

            if(l1<=r2 and l2<=r1):
                if((n1+n2)%2==1):return max(l1,l2)
                return (max(l1,l2)+min(r1,r2))/2
            elif(l1>r2):high = mid1-1
            else:low = mid1+1

        pass
        




            


    
arr1 = [int(i) for i in input().strip().split()]
arr2 = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.findMedianSortedArrays(arr1,arr2))