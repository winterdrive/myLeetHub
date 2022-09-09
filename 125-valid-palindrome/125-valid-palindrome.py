class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaLower={
            "a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M",
            "n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z",
            "0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"
        }
        alphaUpper={
            "A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g","H":"h","I":"i","J":"j","K":"k","L":"l","M":"m",
            "N":"n","O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z",
            "0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"
        }
        forward=0
        reverse=-1
        while(True):
            if forward+abs(reverse)>len(s):
                return True
            if s[forward] not in alphaLower and s[forward] not in alphaUpper:
                forward+=1
                continue
            if s[reverse] not in alphaLower and s[reverse] not in alphaUpper:
                reverse-=1
                continue
            if s[forward] in alphaLower and (s[forward]==s[reverse] or alphaLower[s[forward]]==s[reverse]):
                forward+=1
                reverse-=1
                continue
            if s[forward] in alphaUpper and (s[forward]==s[reverse] or alphaUpper[s[forward]]==s[reverse]):
                forward+=1
                reverse-=1
                continue
            return False
        return True