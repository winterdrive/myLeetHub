class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        myMap=dict()
        result=[]
        for j in range(0,len(heights)):
            myMap[heights[j]]=names[j]
        for key in sorted(myMap):
            result.append(myMap[key])
        return result[::-1]  