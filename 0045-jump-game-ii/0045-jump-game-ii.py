class Solution:
    def jump(self, nums: list[int]) -> int:
        l=0
        r=0
        result=0
        while r < len(nums)-1:
            myMax=0
            for i in range(l,r+1):
                myMax=max(myMax,i+nums[i])
            l=r+1
            r=myMax
            result+=1
        # print(result)
        return result