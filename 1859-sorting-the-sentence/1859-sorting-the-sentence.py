class Solution:
    def sortSentence(self, s: str) -> str:
        result=''
        myDict=dict()
        for i in s.split(' '):
            myDict[i[-1]+i[:-1]]=''
        for value in sorted(myDict):
            result=result+value[1:]+" "
        return result[:-1]