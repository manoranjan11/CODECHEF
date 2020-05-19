N = int(input())

traffic = []
way = {}
for i in range(0,N):
  temp = int(input())
  traffic.append(temp)
  way[i+1] = []

for i in range(0,N-1):
  x,y = map(int,input().split())
  
  way[x] = way[x].append(y)
  way[y] = way[y].append(x)
    
