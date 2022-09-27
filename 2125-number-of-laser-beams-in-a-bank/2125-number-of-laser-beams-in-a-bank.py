class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result=0
        currentLaserNum=0
        formerLaserNum=0
        for i in range(0,len(bank)):
            if (i+1)>len(bank):
                break
            if bank[i].count("1")!=0:
                currentLaserNum=bank[i].count("1")
                result+=formerLaserNum*currentLaserNum
                formerLaserNum=currentLaserNum
        return result