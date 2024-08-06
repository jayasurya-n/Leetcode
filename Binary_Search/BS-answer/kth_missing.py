class Solution:


    def canPlaceCows(self,arr,c,minDistance):
        last = arr[0]
        cows = 1

        for i in range(0,len(arr)):
            if(arr[i]-last>=minDistance):
                cows+=1
                last = arr[i]
            if(cows>=c):
                return True
        return False


    def findLargestMininumDistance(self, arr: list[int], n: int,c:int) -> int:
        arr.sort()
        
        low = 1
        high = arr[n-1] - arr[0]

        ans = -1
        while(low<=high):
            mid = (low+high)//2

            if(self.canPlaceCows(arr,c,mid)):
                ans = max(ans,mid)
                low = mid+1
            else:high = mid-1 

        return ans
        pass
        




            


       



m,c = [int(i) for i in input().strip().split()]
arr = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.findLargestMininumDistance(arr,m,c))