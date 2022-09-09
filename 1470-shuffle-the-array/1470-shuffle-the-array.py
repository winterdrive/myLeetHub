class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        for i in range(0,n):
            result=result+[nums[i]]+[nums[i+n]]
        return result
        
#         result=[]
#         for i in range(0,n):
#             result.append(nums[i])
#             result.append(nums[i+n])
#         return result
        
        # result=[]
        # for i in range(0,n):
        #     result+=[nums[i]]
        #     result+=[nums[i+n]]
        # return result