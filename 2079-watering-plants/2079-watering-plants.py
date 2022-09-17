class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result=0
        currentCap=capacity
        for i in range(0,len(plants)):
            if currentCap-plants[i]>=0:
                result+=1
                currentCap-=plants[i]
                continue
            else:
                result+=((i)+(i+1))
                currentCap=capacity-plants[i]              
        return result