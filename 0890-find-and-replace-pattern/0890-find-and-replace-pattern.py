class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        result=list()
        myList=list(pattern)
        myDict=dict()
        for i in range(len(pattern)):
            if pattern[i] in myDict:
                continue
            else:
                myDict[pattern[i]]=i
        for i in range(len(pattern)):
            myList[i]=myDict[pattern[i]]

        for target in words:
            targetList=list(target)
            myTargetDict=dict()
            for j in range(len(target)):
                if target[j] in myTargetDict:
                    continue
                else:
                    myTargetDict[target[j]]=j
            for k in range(len(target)):
                targetList[k]=myTargetDict[target[k]]
            if myList==targetList:
                result.append(target)
        return result