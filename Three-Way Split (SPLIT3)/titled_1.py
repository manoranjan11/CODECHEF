N = int(input())

traffic = {}
way = {}
for i in range(0,N):
  temp = int(input())
  traffic[i+1] = temp
  way[i+1] = []

for i in range(0,N-1):
  x,y = map(int,input().split())
  
  way[x] = way[x].append(y)
  way[y] = way[y].append(x)

cost1 = 0
cost2 = 0
cost3 = 0

nodes_crossed = []
possibilities = []

def travel(start_node,end_node):
 
  
for i in range(0,N-1):
    for j in range(i,N):
      travel(i,j)
