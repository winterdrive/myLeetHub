class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result=list()
        for i in range(len(nums)):
            result.append(nums[i])
        return result+result