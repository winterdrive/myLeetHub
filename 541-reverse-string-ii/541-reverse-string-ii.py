class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count=0
        for i in range(0,len(s),k):
            if(count%2==0):
                s=s.replace(s[k*count:k+k*count],s[k*count:k+k*count][::-1])
                count+=1
            else:
                count+=1
        return s
