class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result=0
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if i==j:
                    result+=mat[i][j]
                if i+j==len(mat[i])-1:
                    result+=mat[i][j]
        if len(mat)%2!=0:
            result-=mat[len(mat)//2][len(mat)//2]
        return result