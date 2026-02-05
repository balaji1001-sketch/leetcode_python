class solution:
    def transformedarray(self,num):
        n=len[num]
        result=0*n
        for i in range(n):
            if i==0:
                result[i]==0
            else:
                newindex=(i+num[i])%n
                result[i]=num[newindex]
        return result
        