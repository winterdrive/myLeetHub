class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result=0
        plusStatusFormer=0
        for i in range(0,len(nums)):
            if i+1>=len(nums):
                return result
            if nums[i]-nums[i+1]>0:
                if plusStatusFormer==0:
                    plusStatusFormer=-1
                    continue
                plusStatusLatter=-1
                if plusStatusFormer!=plusStatusLatter:
                    result+=1
                plusStatusFormer=plusStatusLatter
            elif nums[i]-nums[i+1]<0:
                if plusStatusFormer==0:
                    plusStatusFormer=1
                    continue
                plusStatusLatter=1
                if plusStatusFormer!=plusStatusLatter:
                    result+=1
                plusStatusFormer=plusStatusLatter
            else:
                pass
            
                
                