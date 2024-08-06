from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # hash = dict()
        # for i in range(len(bills)):
        #     change = bills[i]-5
        #     if(change==15):
        #         if(hash.get(10,0)>=1 and hash.get(5,0)>=1):
        #             hash[10]-=1;hash[5]-=1
        #         elif(hash.get(5,0)>=3):
        #             hash[5]-=3
        #         else:return False
        #     elif(change==5):
        #         if(hash.get(5,0)>=1):
        #             hash[5]-=1
        #         else:return False
        #     hash[bills[i]] = hash.setdefault(bills[i],0)+1
        # return True
        
        five,ten = 0,0
        for i in range(len(bills)):
            if(bills[i]==5):five+=1
            elif(bills[i]==10):ten+=1;five-=1
            else:
                if(ten>0):ten-=1;five-=1
                else:five-=3
            if(five<0):return False
        return True
            
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        bills = list(map(int,input().strip().split()))
        print(Solution().lemonadeChange(bills))