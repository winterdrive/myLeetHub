def myStep(n,k):
    result=n
    stepNum=k
    if result%2==0:
        result=result//2
    else:
        result=result-1
    stepNum+=1
    if result>1:
        return myStep(result,stepNum)
    elif result==1:
        return stepNum+1
    else:
        return stepNum

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==1:
            return 1
        elif num==0:
            return 0
        else:
            return myStep(num,0)