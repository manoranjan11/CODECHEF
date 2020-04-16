T = int(raw_input())


for i in range(0,T):
  N = input()
  N = int(N)
  
  sum = 0
  sequence = raw_input().split(" ")
  
  sequence = [long(i) for i in sequence] 
  
  for j in range(0,len(sequence)-1):
       if j == 0:
            sum = (sum + (sequence[j]*sequence[k]*(2**(N+1-k))))%(1000000007)
        else:
            sum = (sum + (sequence[j]*sequence[k]*(2**(N-(k-j)))))%(1000000007)
      
  print sum
