class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#         sol.1
        result=list()
        currentNum=0
        for i in range(len(nums)):
            currentNum+=nums[i]
            result.append(currentNum)
        return result    
#         sol.2
        # for i in range(1,len(nums)):
        #     nums[i]+=nums[i-1]
        # return nums