class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashDict1 = dict()
        hashDict2 = dict()

        if(len(s)!=len(t)):return False

        for s_i,t_i in zip(s,t):
            if s_i in hashDict1:
                if(hashDict1[s_i]!=t_i):return False
            else:hashDict1[s_i] = t_i

            if t_i in hashDict2:
                if(hashDict2[t_i]!=s_i):return False
            else:hashDict2[t_i] = s_i
        return True





s,t = list(map(str,input().strip().split()))
print(Solution().isIsomorphic(s,t))