class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,j in zip(range(0,len(nums)),range(1,len(nums)+1)):
            if (nums[i]<target) and (nums[-j]>target):
                pass
            else:
                if nums[i]>target:
                    return i
                elif nums[i]==target:
                    return i
                elif nums[-j]<target:
                    return len(nums)+1-j
                elif nums[-j]==target:
                    return len(nums)-j