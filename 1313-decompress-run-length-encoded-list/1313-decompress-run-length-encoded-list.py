class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        repeatNum=0
        for i in range(0,len(nums)):
            if(i%2==0):
                repeatNum=nums[i]
                continue
            for j in range(0,repeatNum):
                result.append(nums[i])
        return result        