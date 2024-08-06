class Solution:
    def bubbleSort(self,arr, n):
        for i in range(n-1,0,-1):
            swap = 0
            for j in range(0,i):
                if(arr[j]>arr[j+1]):
                    arr[j+1],arr[j] = arr[j],arr[j+1]
                    swap = 1
            if(swap==0):break
        return arr



arr = list(map(int,input().strip().split()))
print(Solution().bubbleSort(arr,len(arr)))