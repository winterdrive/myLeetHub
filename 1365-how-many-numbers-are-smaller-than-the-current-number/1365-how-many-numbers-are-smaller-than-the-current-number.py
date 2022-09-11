class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArr = nums.copy()
        newArr.sort()
        dic = {}
        for idx in range(len(newArr)):
            if newArr[idx] not in dic:
                dic[newArr[idx]] = idx
        ans = []
        for elem in nums:
            ans.append(dic[elem])
        return ans 
