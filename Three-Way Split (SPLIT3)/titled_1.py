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

discontinuity = 0
possibilities = []
path = []

def travel(start_node,end_node):
  path = path.append(start_node)
  for node in way[start_node]:
    if node == end_node:
      path.append(node)
      return 1
  
  length = len(path)
  for node in way[start_node]: 
    size = len(way[node])
    if size == 1 | node == path[length - 1]:
      continue
    else:
      discontinuity = discontinuity + size - 2
      if discontinuity>2:
        continue
      temp = travel(node,end_node)
      return 1
  discontinuity = discontinuity - size + 2
  path = path.remove(node)
  return 0    
  
for i in range(0,N-1):
    for j in range(i+1,N):
      temp = travel(i,j)
      if discontinuity == 2:
        for k in path:
          cost1 = cost1 + traffic[k]
