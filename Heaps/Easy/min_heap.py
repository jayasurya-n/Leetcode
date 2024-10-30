from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Heap:
    def __init__(self):
        self.heap = []
    
    def heapifyUp(self,i):
        while(i>0):
            p = (i-1)//2 
            if(self.heap[p]>self.heap[i]):
                self.heap[i],self.heap[p] = self.heap[p],self.heap[i]
                i = p
            else:break

    def heapifyDown(self,i):
        size = len(self.heap)
        if(i>=size):return 
        
        smallest = i
        left = 2*i+1
        right = 2*i+2
        
        if(left<size and self.heap[left]<self.heap[smallest]):smallest = left
        if(right<size and self.heap[right]<self.heap[smallest]):smallest = right
        
        if(smallest!=i):
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i]
            self.heapifyDown(smallest)
        
    def insert(self,x):
        self.heap.append(x)
        self.heapifyUp(len(self.heap)-1)
        
    def delete(self,i):
        if(i<0 or i>=len(self.heap)):return
        self.heap.pop()
        if(self.heap[i]<self.heap[(i-1)//2]):self.heapifyUp(i)
        else:self.heapifyDown(i)

    def extractMin(self):
        if(len(self.heap)==0):return None
        if(len(self.heap)==1):return self.heap.pop()
        ans = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return ans

class Solution:
    def minHeap(self,n: int, Q: [[]]) -> []:
        heap = Heap()
        ans = []
        for i in range(n):
            if(Q[i][0]==0):heap.insert(Q[i][1])
            else:ans.append(heap.extractMin())
        return ans
    
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        Q = []
        for i in range(n):Q.append(list(map(int,input().strip().split())))
        print(Solution().minHeap(n,Q))