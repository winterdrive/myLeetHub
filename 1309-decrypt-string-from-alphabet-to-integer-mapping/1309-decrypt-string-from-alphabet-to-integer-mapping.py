class Solution:
    def freqAlphabets(self, s: str) -> str:
        result=""
        myList=s.split("#")
        print(myList)
        myDict={
            '1':'a',
            '2':'b',
            '3':'c',
            '4':'d',
            '5':'e',
            '6':'f',
            '7':'g',
            '8':'h',
            '9':'i',
            '10':'j',
            '11':'k',
            '12':'l',
            '13':'m',
            '14':'n',
            '15':'o',
            '16':'p',
            '17':'q',
            '18':'r',
            '19':'s',
            '20':'t',
            '21':'u',
            '22':'v',
            '23':'w',
            '24':'x',
            '25':'y',
            '26':'z'
        }
        for i in range(len(myList)):
            if i==len(myList)-1:
                if len(myList[i])==0:
                    break
                currentStr=myList[i]
                while len(currentStr)!=1:
                    result+=myDict[currentStr[0]]
                    currentStr=currentStr[1:]
                result+=myDict[currentStr]
                break
            if myList[i] in myDict:
                result+=myDict[myList[i]]
            else:
                currentStr=myList[i]
                while currentStr not in myDict:
                    result+=myDict[currentStr[0]]
                    currentStr=currentStr[1:]
                result+=myDict[currentStr]
        print(result)
        return result
    