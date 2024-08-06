class Solution: 
    def select(self, arr, i):
        min = i
        for j in range(i,len(arr)):
            if(arr[j]<arr[min]):min = j
        return min
            
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min = self.select(arr,i)
            arr[min],arr[i] = arr[i],arr[min]
        return arr



arr = list(map(int,input().strip().split()))
print(Solution().selectionSort(arr,len(arr)))