class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        result=0
        myDict=dict()
        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]]=1
            else:
                myDict[nums[i]]+=1
        for i in nums:
            if i+k in myDict:
                result+=myDict[i+k]
        # print(result)
        return result