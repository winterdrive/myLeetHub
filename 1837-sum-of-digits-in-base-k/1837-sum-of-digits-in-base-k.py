class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n==1:
            return 1
        if n==k:
            return n//k
        result=0
        tempn=n
        tempk=k
        myPower=0
        while n>tempk**myPower:
            myPower+=1
        myPower-=1
        while myPower>=0:
            tempTime=(tempn//(tempk**myPower))*(tempk**myPower)
            result+=tempn//(tempk**myPower)
            tempn-=tempTime
            myPower-=1
        return result