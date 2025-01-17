from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     hash = [0]*26
    #     for ch in s1:hash[ord(ch)-97]+=1
        
    #     i,j = 0,0
    #     while(j<len(s2)):
    #         hash[ord(s2[j])-97]-=1
    #         while(i<=j and hash[ord(s2[j])-97]<0):
    #             hash[ord(s2[i])-97]+=1
    #             i+=1
            
    #         j+=1
    #         # print("i,j",i,j)
    #         # print(hash)
    #         bool = True
    #         for k in range(26):
    #             if(hash[k]!=0):
    #                 bool = False
    #                 break
    #         if(bool):return True
        
    #     return False
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0]*26
        freq_window = [0]*26
        
        if(len(s1)>len(s2)):return False
        
        for i in range(len(s1)):
            freq_s1[ord(s1[i])-97]+=1
            freq_window[ord(s2[i])-97]+=1
        
        if(freq_s1==freq_window):return True
        
        for i in range(len(s1),len(s2)):
            freq_window[ord(s2[i])-97]+=1
            freq_window[ord(s2[i-len(s1)])-97]-=1
            
            if(freq_s1==freq_window):return True
        
        return False
            

# time complexity: O(l1+26*l2), O(l1+26*(l2-l1))
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s1 = input().strip()
        s2 = input().strip()
        print(Solution().checkInclusion(s1,s2))