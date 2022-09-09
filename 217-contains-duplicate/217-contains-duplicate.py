class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i=0
        resultDict=dict()
        while(True):
            if i==len(nums):
                return False
            if nums[i] not in resultDict:
                resultDict[nums[i]]=1
            else:
                return True
            i+=1