class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result=list()
        m=len(s)
        
        for k in range(0,m):
            count=0
            posX=startPos[0]
            posY=startPos[1]
            for i in s[0+k:m]:
                if i=='R':
                    if posY+1<n:
                        posY=posY+1
                        count+=1
                    else:
                        k+=1
                        break
                elif i=='L':
                    if posY-1>=0:
                        posY=posY-1
                        count+=1
                    else:
                        k+=1
                        break
                elif i=='U':
                    if posX-1>=0:
                        posX=posX-1
                        count+=1
                    else:
                        k+=1
                        break
                elif i=='D':
                    if posX+1<n:
                        posX=posX+1
                        count+=1
                    else:
                        k+=1
                        break
            result.append(count)
        return result