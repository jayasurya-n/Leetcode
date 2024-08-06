class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if(len(t)>len(s)):return ""
        # ans = ""
        # hash = dict()
        # for i in range(len(t)):
        #     hash[t[i]] = hash.setdefault(t[i],0)+1
        # for i in range(len(s)):
        #     check = dict(hash)
        #     for j in range(i,len(s)):
        #         if(s[j] not in check):continue
        #         check[s[j]]-=1
        #         if(check[s[j]]==0):del check[s[j]]
        #         if(len(check))==0:
        #             if(ans=="" or len(ans)>=j-i+1):ans = s[i:j+1]
        # return ans

        if(len(t)>len(s)):return ""

        hash = [0]*256
        for i in range(len(t)):
            hash[ord(t[i])]+=1

        ans = ""
        minLength = 1e9
        i,j = 0,0
        cnt = 0

        while(j<len(s)):
            if(hash[ord(s[j])]>0):cnt+=1
            hash[ord(s[j])]-=1
            while(cnt==len(t)):
                if(j-i+1<minLength):
                    minLength = j-i+1
                    ans = s[i:j+1]
                hash[ord(s[i])]+=1
                if(hash[ord(s[i])]>0):cnt-=1
                i+=1
            j+=1
        return ans
            

# time complexity: O(n^2+m) in first case, o(2n+m) in second case
# space complexity: O(256) in both cases 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s,k = input().strip().split()
        print(Solution().minWindow(s,k))