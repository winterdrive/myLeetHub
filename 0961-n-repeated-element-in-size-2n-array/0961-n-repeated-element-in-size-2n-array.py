class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mySet=set()
        for i in  nums:
            if i not in mySet:
                mySet.add(i)
            else:
                return i
        