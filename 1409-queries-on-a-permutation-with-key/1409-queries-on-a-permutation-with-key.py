class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result=list()
        myList=list(range(1,m+1)) #myList=[1,2,3,4,5]
        for i in queries: #queries = [3,1,2,1]
            resultInt=myList.index(i)
            result.append(resultInt)
            del myList[resultInt]
            myList=[i]+myList
        return result