class Solution:

    def generate(self, numRows: int) -> list[list[int]]:
        pascals_list = []
        for i in range(1,numRows+1):
            pascals_list.append(self.generate_row(i))
        return pascals_list
    
    def generate_row(self,row:int) -> list[int]:
        row_list = []
        ans = 1
        row_list.append(ans)
        for col in range(1,row):
            ans = ans*(row-1-(col-1))
            ans = ans/col
            row_list.append(int(ans))
        return row_list

    

rows = int(input())
obj = Solution()
print(obj.generate(rows))