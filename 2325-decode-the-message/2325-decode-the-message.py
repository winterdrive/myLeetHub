class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        result=""
        alpha='abcdefghijklmnopqrstuvwxyz'
        myDict=dict()
        myDict[" "]=" "
        for i in range(0,len(key)):
            if key[i] not in myDict:
                myDict[key[i]]=alpha[0]
                alpha=alpha[1:]
                if(len(alpha)==0):
                    break
        # print(myDict)        
        for i in range(0,len(message)):
            result+=myDict[message[i]]
        return result