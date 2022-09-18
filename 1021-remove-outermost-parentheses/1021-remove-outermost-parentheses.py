class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=""
        tempStr=''
        front=0
        end=0
        for i in s:
            if i =='(':
                front+=1
                tempStr+='('
            else:
                end+=1
                tempStr+=')'
            if front==end:
                result=result+tempStr[1:-1]
                front=0
                end=0
                tempStr=""
        return result
                