class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result=""
        myNum=0
        for i in range(0,len(word)):
            if word[i]==ch:
                result+=word[i]
                myNum=i
                break
            else:
                result+=word[i]
        if myNum==0:
            # print(result)
            return word
        else:
            result=result[::-1]+word[i+1:]
            # print(result)
            return result