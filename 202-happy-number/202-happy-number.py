class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        exist=set()
        strN=str(n)
        sum=0
        while(sum!=68 and sum!=86 and sum!=1):
            sum=0
            for i in strN:
                sum=sum+int(i)*int(i)
            if sum in exist:
                return False
            exist.add(sum)
            strN=str(sum)
        return True
