class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result=0
        for i in sentences:
            if result<len(i.split(" ")):
                result=len(i.split(" "))
        return result