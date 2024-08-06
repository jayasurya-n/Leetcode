class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):return False

        # Wrong Solution  
        # rotations = -1
        # for i in range(len(goal)):
        #     if(s[0]==goal[i]):
        #         if(i==0):rotations=0
        #         else:rotations = len(s)-i
        
        # for i in range(len(s)):
        #     rotated_i = i-rotations
        #     if(rotated_i<0):rotated_i+=len(s)
        #     if(s[i]!=goal[rotated_i]):return False

        # return True
        
        s = s+s
        if(goal in s):return True
        return False 






s,t = list(map(str,input().strip().split()))
print(Solution().rotateString(s,t))