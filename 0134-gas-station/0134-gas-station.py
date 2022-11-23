class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:
            return -1
        myTotal=0
        for i in range(len(gas)):
            myTotal=myTotal+gas[i]-cost[i]  
            if myTotal<0:
                myTotal=0
            elif myTotal>=0 and myTotal==gas[i]-cost[i]:
                result=i
        return result