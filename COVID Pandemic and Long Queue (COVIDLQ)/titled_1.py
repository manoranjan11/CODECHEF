# cook your dish here
# perfect code
T = int(input())

for i in range(0,T):
  N = int(input())
  
  A = list(map(int,input().split()))
  
  temp = 10 #temporary variable
  status = 0 #status of the text case
  for i in range(0,len(A)):
    if A[i] == 0 & temp == 10: #checking the first person in the queue
      continue
    elif A[i]==0:
      temp = temp+1
    else:
      if temp<5:  
        print("NO")
        status = 1
        break
      temp = 0
      
  if status==0:
    print("YES")
