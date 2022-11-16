class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # result=list()
        # for i in range(len(arr)):
        #     if i == len(arr)-1:
        #         result.append(-1)
        #     else:
        #         result.append(max(arr[i+1:]))
        # return result

        myMax=-1
        for i in range(-1,-(len(arr)+1),-1):
            if i == -1:
                myMax=arr[i]
                arr[i]=-1
            else:
                myTemp=arr[i]
                arr[i]=myMax
                if myTemp>myMax:
                    myMax=myTemp  
        # print(arr)
        return arr