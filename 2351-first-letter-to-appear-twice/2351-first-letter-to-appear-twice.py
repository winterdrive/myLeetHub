class Solution:
    def repeatedCharacter(self, s: str) -> str:
        myDict=dict()
        for i in s:
            if i not in myDict:
                myDict[i]=1
            else:
                myDict[i]+=1
                if myDict[i]==2:
                    return i
        