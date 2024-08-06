class Solution:

    def kthElement(self,  arr1, arr2, n1, n2, k):

        if(n1>n2):return self.kthElement(arr2,arr1,n2,n1,k)
        low = max(0,k-n2)
        high = min(k,n1)

        while(low<=high):
            mid1 = (low+high)//2
            mid2 = k - mid1
            l1,l2 = -1e7,-1e7
            r1,r2 = 1e7,1e7
            if(mid1<n1):r1 = arr1[mid1]
            if(mid2<n2):r2 = arr2[mid2]
            if(mid1-1>=0):l1 = arr1[mid1-1]
            if(mid2-1>=0):l2 = arr2[mid2-1]

            if(l1<=r2 and l2<=r1):
                return max(l1,l2)
            elif(l1>r2):high = mid1-1
            else:low = mid1+1

        pass
        




             
n,m,k = [int(i) for i in input().strip().split()]
arr1 = [int(i) for i in input().strip().split()]
arr2 = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.kthElement(arr1,arr2,n,m,k))