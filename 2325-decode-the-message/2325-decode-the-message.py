class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        result=""
        alpha='abcdefghijklmnopqrstuvwxyz'
        myDict=dict()
        for i in range(0,len(key)):
            if key[i]==" ":
                continue
            if len(myDict.keys())==26:
                break
            if key[i] not in myDict:
                myDict[key[i]]=alpha[0]
                alpha=alpha[1:]
        # print(myDict)        
        for i in range(0,len(message)):
            if(message[i]==" "):
                result+=" "
            else:
                result+=myDict[message[i]]
        return result