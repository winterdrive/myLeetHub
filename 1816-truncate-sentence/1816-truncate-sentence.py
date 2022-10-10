class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        mySplit=s.split(" ")
        return " ".join(mySplit[:k])