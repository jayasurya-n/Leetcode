class Solution:
    def partition(self,arr,low,high):
        pivot = low
        i,j = low,high
        while(i<j):
            while(arr[i]<=arr[pivot] and i<=high-1):i+=1
            while(arr[j]>arr[pivot] and j>=low+1):j-=1
            if(i<j):arr[j],arr[i] = arr[i], arr[j]
        arr[pivot],arr[j] = arr[j],arr[pivot]
        return j

    
    def quickSort(self,arr,low,high):
        if(low>=high):return
        partitionIndex = self.partition(arr,low,high)
        self.quickSort(arr,low,partitionIndex-1) 
        self.quickSort(arr,partitionIndex+1,high) 



arr = list(map(int,input().strip().split()))
Solution().quickSort(arr,0,len(arr)-1)
print(arr)