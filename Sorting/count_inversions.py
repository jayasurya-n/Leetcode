from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def merge(self,arr,low,mid,high):
        cnt = 0
        temp = [0]*(high-low+1)
        i = low
        j = mid+1
        k = 0
        
        while(i<=mid and j<=high):
            if(arr[i]<=arr[j]):
                temp[k] = arr[i]
                i+=1
            else:
                temp[k] = arr[j]
                j+=1
                cnt+=mid-i+1
            k+=1
        
        while(i<=mid):
            temp[k] = arr[i]
            i+=1
            k+=1

        while(j<=high):
            temp[k] = arr[j]
            j+=1
            k+=1
        
        for k in range(0,len(temp)):
            arr[low+k] = temp[k]
        
        return cnt
    
    def inversionCount(self, arr, n):
        def mergeSort(arr,low,high):
            if(low>=high):return 0
            cnt = 0
            mid = (high+low)//2
            cnt+=mergeSort(arr,low,mid)
            cnt+=mergeSort(arr,mid+1,high)
            cnt+=self.merge(arr,low,mid,high)
            return cnt
        return mergeSort(arr,0,len(arr)-1)

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().inversionCount(arr,len(arr)))