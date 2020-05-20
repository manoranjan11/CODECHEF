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

cost = 0

discontinuity = 0
discontinuity_nodes = []
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
      discontinuity_nodes = discontinuity_nodes.append(start_node
                                                      )
      if discontinuity>2:
        continue
      temp = travel(node,end_node)
      return 1
  discontinuity = discontinuity - size + 2
  path = path.remove(node)
  discontinuity_nodes = discontinuity_nodes.remove(node)
  return 0    

def calculate(node):
  for n in way[node]:
    if n not in path:
      cost = cost + traffic[n]
      if len(way[n]) !=1:
        calculate(n)
             
for i in range(0,N-1):
    for j in range(i+1,N):
      temp = travel(i,j)
      if discontinuity == 2:
        for k in path:
          cost = cost + traffic[k]
        discontinuity = 0
       
        option = []
        option = option.append(cost)
        cost = 0
        
        for k in discontinuity_nodes:
          for node in way[k]:
            if node not in path:
              calculate(node)
              option = option.append(cost)
              cost = 0
      possibilities = possibilities.append(option)
      
