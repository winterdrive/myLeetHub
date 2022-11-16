class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # nums.length == 2 * n
        mySet=set()
        for i in nums:
            if i not in mySet:
                mySet.add(i)
            else:
                mySet.remove(i)
        if len(mySet)>0:
            return False
        return True