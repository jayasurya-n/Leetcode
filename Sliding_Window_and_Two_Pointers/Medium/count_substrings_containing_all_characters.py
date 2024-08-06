from typing import List
class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    # i,j=0,0
    # ans = 0
    # hash = dict()
    # while(j<len(s)):
    #     hash[s[j]] = hash.setdefault(s[j],0)+1
    #     if(len(hash)==3):
    #         ans+=len(s)-j
    #         while(len(hash)==3):
    #             hash[s[i]]-=1
    #             if(hash[s[i]]==0):del hash[s[i]]
    #             if(len(hash)==3):ans+=len(s)-j
    #             i+=1
    #     j+=1   
    # return ans

    # lastSeen = [-1]*3
    # ans = 0
    # for i in range(len(s)):
    #     lastSeen[ord(s[i])-ord('a')]=i
    #     if(lastSeen[0]!=-1 and lastSeen[1]!=-1 and lastSeen[2]!=-1):
    #        ans+=1+min(lastSeen[0],lastSeen[1],lastSeen[2])
    # return ans 

    lastSeen = [-1]*3
    ans = 0
    for i in range(len(s)-1,-1,-1):
        lastSeen[ord(s[i])-ord('a')]=i
        if(lastSeen[0]!=-1 and lastSeen[1]!=-1 and lastSeen[2]!=-1):
           ans+=len(s)-max(lastSeen[0],lastSeen[1],lastSeen[2])
    return ans 

            


# time complexity: O(2n) in first case, O(n) in second and third case
# space complexity: O(3) in all cases
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        print(Solution().numberOfSubstrings(s))