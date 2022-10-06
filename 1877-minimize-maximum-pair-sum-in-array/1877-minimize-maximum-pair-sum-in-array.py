class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sortedNums=sorted(nums)
        myList=list()
        for i in range(0,len(nums)//2):
            myList.append(sortedNums[i]+sortedNums[-i-1])
        # print(max(myList))
        return max(myList)