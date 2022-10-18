class Solution:
    def minOperations(self, nums: list[int]) -> int:
        result=0
        if len(nums)==1:
            return 0
        myMax=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=myMax:
                myMax+=1
                result+=(myMax-nums[i])
            else:
                myMax=nums[i]
        print(result)
        return result