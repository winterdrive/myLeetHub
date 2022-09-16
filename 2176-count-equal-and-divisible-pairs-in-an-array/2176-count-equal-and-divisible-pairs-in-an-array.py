class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result=0
        myDict=dict()
        for i in range(0,len(nums)):
            if nums[i] in myDict:
                myDict[nums[i]].append(i)
            else:
                myDict[nums[i]]=[i]
        for key,value in myDict.items():
            if(len(value)>1):
                count=0
                for i in range(0,len(value)):
                    for j in range(1+i,len(value)):
                        if ((value[i]*value[j])%k)==0:
                            count+=1
                result+=(count)
        return result