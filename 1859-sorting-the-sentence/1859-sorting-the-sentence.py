class Solution:
    def sortSentence(self, s: str) -> str:
        result=''
        myList=s.split(' ')
        myDict=dict()
        for i in myList:
            myDict[i[-1]+i[:-1]]=''
        myDict=sorted(myDict)
        for value in myDict:
            result=result+value[1:]+" "
        return result[:-1]