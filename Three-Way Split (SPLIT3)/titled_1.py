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

cost1 = 0
cost2 = 0
cost3 = 0

nodes_left = N
possibilities = []

def travel(start_index):
  for i in len(way[start_index]):
    
  
for i in range(0,N-1):
  if len(way[i+1]) == 1:
    travel(i+1)
