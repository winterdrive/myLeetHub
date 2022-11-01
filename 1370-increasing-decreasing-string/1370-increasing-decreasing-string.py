class Solution:
    def sortString(self, s: str) -> str:
        result=""
        s=list(s)
        myStrSet=sorted(set(s))
        myStrSetReverse=sorted(set(s))[::-1]
        while len(s)!=0:
            for i in myStrSet: #處理遞減
                if len(s)==0:
                    break
                if i not in s:
                    continue
                s.remove(i)
                result+=i
            for i in myStrSetReverse: #處理遞增
                if len(s)==0:
                    break
                if i not in s:
                    continue
                s.remove(i)
                result+=i
        # print(result)
        return result