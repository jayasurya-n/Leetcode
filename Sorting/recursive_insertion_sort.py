class Solution: 
    def recursiveInsertion(self,arr,index,n):
        if(index==n):return
        i = index
        while(i>0 and arr[i]<arr[i-1]):
            arr[i-1],arr[i] = arr[i],arr[i-1]
            i-=1
        self.recursiveInsertion(arr,index+1,n)

    def insertionSort(self, arr, n):
        self.recursiveInsertion(arr,1,n)


arr = list(map(int,input().strip().split()))
Solution().insertionSort(arr,len(arr))
print(arr)