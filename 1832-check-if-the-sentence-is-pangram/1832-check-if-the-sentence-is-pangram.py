class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        mySet=set()
        for i in sentence:
            mySet.add(i)
            if len(mySet)==26:
                return True
        return False