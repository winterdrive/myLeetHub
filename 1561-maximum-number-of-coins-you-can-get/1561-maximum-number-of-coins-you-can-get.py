class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        result=0
        myPiles=sorted(piles,reverse=True)
        while len(myPiles)>=3:
            result+=myPiles[1]
            myPiles.pop(0)
            myPiles.pop(0)
            myPiles.pop()
        print (result)
        # print (myPiles)
        return result