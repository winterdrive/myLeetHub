class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        myProduct=1
        mySum=0
        for i in str(n):
            myProduct*=int(i)
            mySum+=int(i)
        return myProduct-mySum