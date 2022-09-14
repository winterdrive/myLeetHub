class Solution:
    def sortSentence(self, s: str) -> str:
        result=''
        myDict=dict()
        for i in s.split(' '):
            myDict[int(i[-1])]=i[:-1]
        for i in range(1,len(s.split(' '))+1):
            result=result+myDict[i]+" "
        return result[:-1]