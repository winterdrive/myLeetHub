class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result=0
        myList=sorted(heights)
        for i,j in zip(heights,myList):
            if i!=j:
                result+=1
        return result
            