def myUnit(num):
    result=0
    for i in str(num):
        result+=int(i)
    return result
        
class Solution:
    def addDigits(self, num: int) -> int:
        result=num
        while result>=10:
            result=myUnit(result)
        return result