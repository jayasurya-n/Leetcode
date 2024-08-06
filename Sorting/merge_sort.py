class Solution:
    def merge(self,arr, low, mid, high):
        temp = [0]*(high-low+1)

        i = low
        j = mid+1
        k = 0

        while(i<=mid and j<=high):
            if(arr[i]<=arr[j]):
                temp[k] = arr[i]
                i+=1
                k+=1
            else:
                temp[k] = arr[j]
                j+=1
                k+=1
        
        while(i<=mid):
            temp[k] = arr[i]
            i+=1
            k+=1
        
        while(j<=high):
            temp[k] = arr[j]
            j+=1
            k+=1

        for k in range(len(temp)):
            arr[low+k] = temp[k]


    def mergeSort(self,arr, low, high):
        if(low>=high):return
        mid = (low+high)//2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
        return



arr = list(map(int,input().strip().split()))
Solution().mergeSort(arr,0,len(arr)-1)
print(arr)