class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    result+=1
        return result