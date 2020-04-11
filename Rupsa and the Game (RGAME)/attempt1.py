T = input()

T = int(T)
total_sum = []

for i in range(0,T):
  N = input()
  N = int(N)
  
  sum = 0
  numbers = input()
  sequence = numbers.split()
  
  sequence = [int(i) for i in sequence] 
  
  for j in range(0,len(sequence)):
    for k in range(j+1,len(sequence)):
      sum = sum + (sequence[j]*sequence[k]*(2**(N+1-k)))
      
  total_sum.append(sum)
  
for i in range(0,len(sequence)):
  print(total_sum[i])
