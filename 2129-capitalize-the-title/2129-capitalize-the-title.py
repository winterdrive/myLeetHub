class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result=""
        myList=title.split(" ")
        for i in range(0,len(myList)):
            if len(myList[i])>2:
                myList[i]=myList[i].lower().capitalize()
            else:
                myList[i]=myList[i].lower()
        return " ".join(myList)
