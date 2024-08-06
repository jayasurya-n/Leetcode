class Solution:
    def insert(self, arr, index, n):
        while(index>0 and arr[index]<arr[index-1]):
            arr[index-1],arr[index] = arr[index],arr[index-1]
            index-=1
                
    def insertionSort(self, arr, n):
        for i in range(1,n):
            self.insert(arr,i,n)
        return arr



arr = list(map(int,input().strip().split()))
print(Solution().insertionSort(arr,len(arr)))