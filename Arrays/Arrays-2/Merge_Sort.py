class Solution:
    def mergeSort(self,arr:list,low:int,high:int):
        if(low>=high):
            return
            
        mid = (high+low)//2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
        pass

    def merge(self,arr,low,mid,high):
        merged = [0 for i in range(high-low+1)]
        i = low
        j = mid+1
        k = 0
        while(i<=mid and j<=high):
            if(arr[i]<=arr[j]):
                merged[k] = arr[i]
                i+=1
                k+=1
            else:
                merged[k] = arr[j]
                j+=1
                k+=1
        
        while(i<=mid):
            merged[k] = arr[i]
            i+=1
            k+=1

        while(j<=high):
            merged[k] = arr[j]
            j+=1
            k+=1
        
        for k in range(0,len(merged)):
            arr[low+k] = merged[k]



    

nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.mergeSort(nums,0,len(nums) - 1))
print(nums)