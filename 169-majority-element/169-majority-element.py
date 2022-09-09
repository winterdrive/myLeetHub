class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i=0
        resultDict=dict()
        while(True):
            if nums[i] not in resultDict:
                resultDict[nums[i]]=1
            else:
                resultDict[nums[i]]=resultDict[nums[i]]+1
            if resultDict[nums[i]]>(len(nums)/2):
                return nums[i]
            i+=1