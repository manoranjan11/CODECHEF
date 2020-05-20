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

def travel(start_node,branches,nodes_passed):
  cost = 0
  
  nodes_passed = nodes_passed.append(start_node)
  for node in way[start_node]:
    branches = branches + len(way[start_node])
  
for i in range(0,N-1):
  if len(way[i+1]) == 1:
    travel(i+1)
