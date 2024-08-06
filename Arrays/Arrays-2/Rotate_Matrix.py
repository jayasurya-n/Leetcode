class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n =  len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(0,n):
            matrix[i].reverse()

        
    
matrix = []
n = int(input())

for i in range(n):
    a = [int(x) for x in input().strip().split()]
    matrix.append(a)


obj = Solution()
obj.rotate(matrix)
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end = " ")
    print()