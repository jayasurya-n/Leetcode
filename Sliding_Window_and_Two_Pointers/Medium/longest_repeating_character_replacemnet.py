from typing import List
class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
        # freq = [0]*26
        # ans = 0;max_freq = 0
        # i,j=0,0
        # while(j<len(s)):
        #     freq[ord(s[j])-ord('A')]+=1
        #     max_freq = max(max_freq,freq[ord(s[j])-ord('A')])
        #     while((j-i+1)-max_freq>k):
        #         freq[ord(s[i])-ord('A')]-=1
        #         max_freq = max(freq) 
        #         i+=1
        #     ans = max(ans,j-i+1)
        #     j+=1
        # return ans

    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        ans = 0;max_freq = 0
        i,j=0,0
        while(j<len(s)):
            freq[ord(s[j])-ord('A')]+=1
            max_freq = max(max_freq,freq[ord(s[j])-ord('A')])
            if((j-i+1)-max_freq>k):
                freq[ord(s[i])-ord('A')]-=1
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans


            


# time complexity: O(2n)*O(26) in first case, O(n)
# space complexity: O(26), O(26)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        k = int(input().strip())
        print(Solution().characterReplacement(s,k))