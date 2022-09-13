class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        myArrary=list()
        myLen=len(grid)
        iterateCount=myLen-3
        for x in range(0,iterateCount+1):
            mySubArray=list()
            for y in range(0,iterateCount+1) :    
                myMax=0
                for i in range(x,myLen):
                    if i>=3+x:
                            break
                    for j in range(y,myLen):
                        if j>=3+y:
                            break
                        if myMax<=grid[i][j]:
                            myMax=grid[i][j]
                mySubArray.append(myMax)
            myArrary.append(mySubArray)
        return myArrary
        


                    
            