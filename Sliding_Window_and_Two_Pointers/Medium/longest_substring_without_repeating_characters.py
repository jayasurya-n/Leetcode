class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # i=0;j=0
        # freq = [0]*256
        # ans = 0
        # while(j<len(s)):
        #     freq[ord(s[j])]+=1
        #     while(i<j and freq[ord(s[j])]>1):
        #         freq[ord(s[i])]-=1
        #         i+=1
        #     ans = max(ans,j-i+1)
        #     j+=1
        # return ans

        i=0;j=0
        freq = [-1]*256
        ans = 0
        while(j<len(s)):
            if(freq[ord(s[j])]!=-1):
                if(freq[ord(s[j])]>=i):i=freq[ord(s[j])]+1
            ans = max(ans,j-i+1)
            freq[ord(s[j])]=j
            j+=1
        return ans


# time complexity: O(2n) in first case, O(n) in second case  
# space complexity: O(256)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        print(Solution().lengthOfLongestSubstring(s))