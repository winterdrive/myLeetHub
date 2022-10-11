class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result=0
        myList=[".-","-...","-.-.","-..",".",
        "..-.","--.","....","..",".---","-.-",
        ".-..","--","-.","---",".--.","--.-",
        ".-.","...","-","..-","...-",".--",
        "-..-","-.--","--.."]
        myAplha=string.ascii_lowercase

        myDict={}

        for i in range(0,len(myAplha)):
            myDict[myAplha[i]]=myList[i]

        mySet=set()
        for i in words:
            tempStr=""
            for j in i:
                tempStr+=myDict[j]
            mySet.add(tempStr)
        # print(mySet)
        # print(len(mySet))
        return len(mySet)
