class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A: tuple[int]):
        # A = list(A)
        # n = len(A)

        # A1 = [0 for i in range(n+1)]

        # repeated,misssing = 0,0
        # for i in range(0,n):
        #     A1[A[i]]+=1

        # for i in range(1,n+1):
        #     if(A1[i]==2):
        #         repeated = i
        #     if(A1[i]==0):
        #         misssing = i
        
        # return (repeated,misssing)

        

        n  = len(A)
        square_sum, sum = 0,0
        act_square_sum, act_sum = 0,0

        for i in range(1,n+1):
            sum+=i
            square_sum+=i*i

        for i in range(0,n):
            act_sum+=A[i]
            act_square_sum+=A[i]*A[i]
        
        diffoftwo = act_sum-sum
        sumoftwo = (act_square_sum-square_sum)/(diffoftwo)

        repeated = int((sumoftwo+diffoftwo)/2)
        misssing = int((sumoftwo-diffoftwo)/2)
        return (repeated,misssing)

        pass

        

A = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.repeatedNumber(A))