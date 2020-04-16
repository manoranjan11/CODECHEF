T = int(raw_input())

for _ in range(0,T):
  N = int(raw_input())
  
  P = list(map(long,raw_input().split()))
    
  profit = 0
  
  P.sort(reverse = True)
  
  for i in range(0,N):
    if P[i] - i < 0:
      profit = profit + P[i] -i
      
  print profit   
