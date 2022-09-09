class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs[0]==""):
            return "" 
        elif(len(strs)==1):
            return strs[0]
        firstStr=strs[0]
        result=""
        for aphlabetNum in range(0,len(firstStr)):
            for itemNum in range(1,len(strs)):
                if (aphlabetNum+1>len(strs[itemNum])):
                    return result
                elif firstStr[aphlabetNum]!=strs[itemNum][aphlabetNum]:
                    return result
                else:
                    if(itemNum==len(strs)-1):
                        result=result+firstStr[aphlabetNum]
                    else:
                        pass
        return result