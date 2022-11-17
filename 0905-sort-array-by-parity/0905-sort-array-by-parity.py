class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        myOdd=list()
        myEven=list()
        for i in range(len(nums)):
            if nums[i]%2!=0:
                myOdd.append(nums[i])
            else:
                myEven.append(nums[i])
        return myEven+myOdd