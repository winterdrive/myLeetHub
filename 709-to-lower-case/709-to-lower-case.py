class Solution:
    def toLowerCase(self, s: str) -> str:
        if len(s)<=26:
            s=s.lower()
        else:
            s=s.replace('A','a').replace('B','b').replace('C','c').replace('D','d').replace('E','e').replace('F','f').replace('G','g').replace('H','h').replace('I','i').replace('J','j').replace('K','k').replace('L','l').replace('M','m').replace('N','n').replace('O','o').replace('P','p').replace('Q','q').replace('R','r').replace('S','s').replace('T','t').replace('U','u').replace('V','v').replace('W','w').replace('X','x').replace('Y','y').replace('Z','z')
        return s

