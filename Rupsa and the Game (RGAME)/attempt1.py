T = int(raw_input())

#my own approach.. got 10% right
#can reduce run time by following the correct answer with the same idea though
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
