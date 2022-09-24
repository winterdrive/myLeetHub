class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        result=0
        myLen=len(arr)
        if myLen==1:
            return arr[0]
        for i in range(1,myLen+1,2):
            tempSum=0
            startIndex=0
            endIndex=i
            for k in range(0,myLen):
                if endIndex>myLen:
                    break
                tempArr=arr[startIndex:endIndex]
                startIndex+=1
                endIndex+=1
                for r in tempArr:
                    tempSum+=r
            result+=tempSum
        return result


