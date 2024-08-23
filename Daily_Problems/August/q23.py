from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def fractionAddition(self, expression: str):
        n,d = 0,1
        if(expression[0]!='-'):expression = '+' + expression
        
        i = 0 
        while(i<len(expression)):
            sign = expression[i]
            i+=1
            
            n1 = 0
            while(i<len(expression) and expression[i].isdigit()):
                n1= n1*10 + int(expression[i])
                i+=1
            
            i+=1
            
            d1 = 0
            while(i<len(expression) and expression[i].isdigit()):
                d1= d1*10 + int(expression[i])
                i+=1

            if(sign=='-'):n1 = -n1
            
            n = n*d1+n1*d
            d = d*d1
            
        gcd_n_d = math.gcd(n,d) 
        n//= gcd_n_d
        d//= gcd_n_d
        return str(n)+"/"+str(d)
        
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().fractionAddition(s))