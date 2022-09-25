class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result=0
        rNum=0
        lNum=0
        for i in s:
            if i=='R':
                rNum+=1
            else:
                lNum+=1
            if rNum==lNum:
                result+=1
        return result