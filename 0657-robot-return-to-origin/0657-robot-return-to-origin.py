class Solution:
    def judgeCircle(self, moves: str) -> bool:
        result=0
        myDict={"U":1,"D":-1,"R":30000,"L":-30000}
        for i in moves:
            result+=myDict[i]
        if result==0:
            return True
        else:
            return False