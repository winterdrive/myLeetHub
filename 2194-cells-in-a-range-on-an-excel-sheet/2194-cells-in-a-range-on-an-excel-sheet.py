class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result=list()
        alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        startIndex=alpha.index(s[0])
        while(True):
            for j in range(int(s[1]),int(s[4])+1):
                result.append(alpha[startIndex]+str(j))
            if alpha[startIndex]==s[3]:
                break
            startIndex+=1
        return result