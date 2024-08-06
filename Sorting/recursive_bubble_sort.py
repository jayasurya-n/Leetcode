class Solution:
    def bubbleSort(self,arr, n):
        if(n==0 or n==1):return
        swap = 0
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = 1
        if(swap==0):return
        self.bubbleSort(arr,n-1) 
            


arr = list(map(int,input().strip().split()))
Solution().bubbleSort(arr,len(arr))
print(arr)