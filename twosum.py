class Solution:
  def twosum(self,num,target):
      seen={}
      for i in range(len[num]):
          diff=target-num[i]
          if diff in seen:
              return[seen[diff],i]
    
              seen[num[i]] = i

      