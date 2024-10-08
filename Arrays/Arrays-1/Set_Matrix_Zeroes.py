class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # row = [0 for i in range(m)]
        # col = [0 for i in range(n)]

        # for i in range(m):
        #     for j in range(n):
        #         if(matrix[i][j]==0):
        #             row[i] = 1
        #             col[j] = 1 
        
        # for i in range(m):
        #     for j in range(n):
        #         if(row[i] | col[j] ):
        #             matrix[i][j] = 0

        col0 = 1
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    matrix[i][0] = 0
                    if(j!=0):
                        matrix[0][j] = 0
                    else:
                        col0 = 0


        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][j]!=0):
                    if((matrix[0][j]==0) | (matrix[i][0]==0)):
                        matrix[i][j] = 0                    
       

        for j in range(n): 
            if(matrix[0][0]==0):
                matrix[0][j] = 0

        for i in range(m): 
            if(col0==0):
                matrix[i][0] = 0
    
matrix = []
m,n = (int(x) for x in input().strip().split())

for i in range(m):
    a = [int(x) for x in input().strip().split()]
    matrix.append(a)


obj = Solution()
obj.setZeroes(matrix)
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end = " ")
    print()