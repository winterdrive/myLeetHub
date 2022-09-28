class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=""
        myDict={}
        for i,j in zip(range(0,len(indices)),s):
            myDict[indices[i]]=j
        for key in sorted(myDict):
            result+=myDict[key]
        return result