class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultMap={}
        for i in range(0,len(nums)):
            remains=target-nums[i]
            if(remains in resultMap and resultMap[remains]!=i):
                return [resultMap[remains],i]
            resultMap[nums[i]]=i

        
        