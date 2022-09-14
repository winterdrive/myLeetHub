class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result=0
        myDict=dict()
        for i in nums:
            if i-diff not in myDict:
                myDict[i]=1
            else:
                myDict[i]=myDict[i-diff]+1
                if myDict[i]>=3:
                    result+=1
        return result
            