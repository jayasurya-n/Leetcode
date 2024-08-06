class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):return False
        # dict1 = dict()
        # dict2 = dict()
        # for i,j in zip(s,t):
        #     dict1[i] = dict1.setdefault(i,0)+1 
        #     dict2[j] = dict2.setdefault(j,0)+1 

        # for key in dict1.keys():
        #     if(dict1.get(key)!=dict2.get(key)):return False
        # return True

        if(sorted(s)==sorted(t)):return True
        return False



s,t = list(map(str,input().strip().split()))
print(Solution().isAnagram(s,t))