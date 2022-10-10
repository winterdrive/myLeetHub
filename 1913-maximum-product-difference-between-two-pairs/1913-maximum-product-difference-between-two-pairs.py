class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sortedNums=sorted(nums)
        myMin=sortedNums[0]*sortedNums[1]
        myMax=sortedNums[-1]*sortedNums[-2]
        return myMax-myMin