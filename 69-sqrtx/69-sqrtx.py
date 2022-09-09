class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x>=1 and x<4:
            return 1
        elif x>=4 and x<9:
            return 2
        lm=0
        rm=x//2
        middle=(lm+rm)//2
        while (lm!=rm):
            if middle*middle>x:
                rm=middle
                middle=(lm+rm)//2
                if rm==middle:
                    return rm
            elif middle*middle<x:
                lm=middle
                middle=(lm+rm)//2
                if lm==middle:
                    return lm
            else:
                return middle
        return rm