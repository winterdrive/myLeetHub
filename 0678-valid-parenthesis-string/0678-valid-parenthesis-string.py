class Solution:
    def checkValidString(self, s: str) -> bool:
        # 這題用greedy解，我們只關注有多少左括號需要配對
        leftMin=0 #左括號最小數量
        leftMax=0 #左括號最大數量

        for i in s:
            if i=="(":
                # 最多最少需要配對的左括號都+1
                leftMin+=1
                leftMax+=1
            elif i==")":
                # 出現又括號，所以需要配對的左括號數量都-1
                leftMin-=1
                leftMax-=1            
            else:
                # 出現wildcard，
                leftMin-=1 # 他當右括號時，需要配對的最小左括號數量-1
                leftMax+=1 # 他當左括號時，需要配對的最大左括號數量+1

            if leftMax<0:
                # 當最大左括號數量已達負數，
                # 則代表當前右括號已經超越左括號數量，不合法
                return False 
            if leftMin<0:
                # 當最小左括號數量已達負數，
                # 代表這次wildcard當右括號決定不正確，他只能當空白或左括號
                # 所以把當右括號時leftMin-1的運算復原(歸零)
                leftMin = 0

        return leftMin == 0
        

