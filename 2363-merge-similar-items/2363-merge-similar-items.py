class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        myDict=dict()
        myList=list()
        result=list()
        for i in items1:
            myDict[i[0]]=i[1]
            myList.append(i[0])
        for i in items2:
            if i[0] not in myDict:
                myDict[i[0]]=i[1]
                myList.append(i[0])
            else:
                myDict[i[0]]+=i[1]
        for i in sorted(myList):
            result.append([i,myDict[i]])
        return result
        