class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result=0
        myLargest=0
        myDict=dict()
        for i in edges:
            for j in i:
                if j not in myDict:
                    myDict[j]=1
                else:
                    myDict[j]+=1
                    if myDict[j]>myLargest:
                        result=j
                        myLargest=myDict[j]
        return result