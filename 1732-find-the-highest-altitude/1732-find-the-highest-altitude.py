class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mySum=0
        myMax=0
        for i in range(len(gain)):
            mySum+=gain[i]
            if mySum>myMax:
                myMax=mySum
        # print(myMax)
        return myMax