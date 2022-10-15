class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        myMaxValue=0
        myMaxKey=0
        myDict=dict()
        for i in rectangles:
            if min(i) not in myDict:
                myDict[min(i)]=1
            else:
                myDict[min(i)]+=1
        for key,value in myDict.items():
            if key>myMaxKey:
                myMaxKey=key
                myMaxValue=value
        return myMaxValue