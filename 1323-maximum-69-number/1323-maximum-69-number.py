class Solution:
    def maximum69Number (self, num: int) -> int:
        i=0
        resultString=str(num)
        stringLength=len(resultString)
        while(True):
            if i>=len(resultString):
                return resultString
            if int(resultString[i])%6==0:
                return int(resultString[:i]+"9"+resultString[i+1:])
            i+=1    
                
                