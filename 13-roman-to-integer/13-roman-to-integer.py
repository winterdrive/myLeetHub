class Solution:
    def romanToInt(self, s: str) -> int:
        finalInt=0
        romanMap={'I':1,
                  'V':5,
                  'X':10,
                  'L':50,
                  'C':100,
                  'D':500,
                  'M':1000
        }
        stopInt=0
        for i in range(0,len(s)):
            if(i==stopInt and i!=0):
                continue
            if(s[i]=='I' and i+1<len(s)):
                if(s[i+1]=='V'):
                    finalInt= finalInt+4
                    stopInt=i+1
                elif(s[i+1]=='X'):
                    finalInt=finalInt+9
                    stopInt=i+1
                else:
                      finalInt= finalInt+romanMap[s[i]]
            elif(s[i]=='X' and i+1<len(s)):
                if(s[i+1]=='L'):
                    finalInt= finalInt+40
                    stopInt=i+1
                elif(s[i+1]=='C'):
                    finalInt=finalInt+90
                    stopInt=i+1
                else:
                      finalInt= finalInt+romanMap[s[i]]
            elif(s[i]=='C' and i+1<len(s)):
                if(s[i+1]=='D'):
                    finalInt= finalInt+400
                    stopInt=i+1
                elif(s[i+1]=='M'):
                    finalInt=finalInt+900
                    stopInt=i+1
                else:
                    finalInt= finalInt+romanMap[s[i]]
            else:
                finalInt= finalInt+romanMap[s[i]]
        return finalInt

# "MCMXCIV"
# 2216
# 1994
        