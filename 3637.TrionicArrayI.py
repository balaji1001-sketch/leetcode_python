class Solution:
    def istrionic(self,num:list[int]) ->bool:
        n=len[num]
        i=1
        if n<3:
            return False
        
        while i<n and num[i]<num[i-1]:
            i+=1
            
        if i==1 or i==n:
            return False
        
        while i<n and num[i]>num[i-1]:
            i+=1
            
        if i==1 or i==n:
            return False
        
        while i<n and num[i]>num[i-1]:
            i+=1
            
        if i==1:
            return True