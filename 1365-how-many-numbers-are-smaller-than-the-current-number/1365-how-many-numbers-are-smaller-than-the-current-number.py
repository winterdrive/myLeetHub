class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSorted=sorted(nums)
        myDict=dict()
        result=list()
        for i in nums:
            if i not in myDict :
                myDict[i]=numsSorted.index(i)
        for i in nums:
            result.append(myDict[i])
        return result