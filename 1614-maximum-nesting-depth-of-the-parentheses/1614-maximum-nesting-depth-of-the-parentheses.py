class Solution:
    def maxDepth(self, s: str) -> int:
        result=0
        myMax=0
        for i in s:
            if i=="(":
                result+=1
                if result>myMax:
                    myMax=result
            elif i==")":
                result-=1
        return myMax