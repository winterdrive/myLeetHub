class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSorted=sorted(nums)
        myDict=dict()
        count=0.0001
        for i in nums:
            if i in myDict :
                myDict[i+count]=numsSorted.index(i)
                count=count+0.0001
            else:
                myDict[i]=numsSorted.index(i)
        return myDict.values()