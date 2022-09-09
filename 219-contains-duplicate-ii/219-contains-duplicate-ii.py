class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        resultDict=dict()#key:[index,dist]
        while(True):
            if i>=len(nums):
                break
            if nums[i] not in resultDict:
                resultDict[nums[i]]=[i,0] #4:[0,0],1[1,0],2[2,0],3[3,0],5[5,0]
                i+=1
            else:
                if resultDict[nums[i]][1]<=0:#1[1,0]->0<=0
                    resultDict[nums[i]]=[i,abs(resultDict[nums[i]][0]-i)]#1:[4,0+4]
                elif abs(resultDict[nums[i]][0]-i)<resultDict[nums[i]][1]:#abs(2-3)=1<2
                    resultDict[nums[i]]=[i,abs(resultDict[nums[i]][0]-i)]#1:[3,2]    
                if resultDict[nums[i]][1]<=k:
                    return True
                i+=1
        return False