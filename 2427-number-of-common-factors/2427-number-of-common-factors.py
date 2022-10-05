class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        result=0
        myMin=min(a,b)
        for i in range(1,myMin+1):
            if a%i==0 and b%i==0:
                result+=1
        return result