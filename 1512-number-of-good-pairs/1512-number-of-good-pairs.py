# from math import factorial
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        myDict=dict()
        result=0
        for i in range(0,len(nums)):
            if nums[i] not in myDict: 
                myDict[nums[i]]=1
            else:
                myDict[nums[i]]=myDict[nums[i]]+1
        for key,value in myDict.items():
            if value>1:
                # result=result+int(factorial(value)/(factorial(value-2)*2))
                result=result+int((value)*(value-1)/(2))
        return result