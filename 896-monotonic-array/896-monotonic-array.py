class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if len(nums)>=2:
            if nums[0]-nums[1]>0:
                rsortedNums=sorted(nums,reverse=True)
                if nums!=rsortedNums:
                    return False
                else:
                    return True
            elif nums[0]-nums[1]<0:
                sortedNums=sorted(nums)
                if nums!=sortedNums:
                    return False
                else:
                    return True
            else:
                sortedNums=sorted(nums)
                if nums==sortedNums:
                    return True
                rsortedNums=sorted(nums,reverse=True)
                if nums==rsortedNums:
                    return True
                return False