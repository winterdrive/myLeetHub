class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        myLen=len(s)
        result=0
        for i in s:
            if i==letter:
                result+=1
        return int((result/myLen)*100)
