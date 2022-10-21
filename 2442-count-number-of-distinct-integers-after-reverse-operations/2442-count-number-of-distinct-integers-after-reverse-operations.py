class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        mySet=set(nums)
        for i in nums:
            mySet.add(int(str(i)[::-1]))
        return len(mySet)