class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for baseNumber in range(2,n):
            myBase2String=list()
            iterateNumber=n
            while iterateNumber!=0:
                myBase2String.append(iterateNumber%baseNumber)
                iterateNumber=iterateNumber//baseNumber
            for i,j in zip(myBase2String,myBase2String[::-1]):
                if i!=j:
                    return False
        return True