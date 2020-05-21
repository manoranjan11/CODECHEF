N = int(input())

traffic = {}
way = {}
for i in range(0,N):
  temp = int(input())
  traffic[i+1] = temp
  way[i+1] = []

for i in range(0,N-1):
  x,y = map(int,input().split())
  
  way[x].append(y)
  way[y].append(x)

cost = 0

discontinuity = 0
discontinuity_nodes = []
possibilities = []
path = []
previous_node = 0

def travel(start_node,end_node):
  global discontinuity
  global previous_node
  path.append(start_node)
   
  for node in way[start_node]:
    if node == end_node:
      path.append(node)
      size1 = len(way[node])
      if size1 != 1:
        discontinuity += size1-1
        discontinuity_nodes.append(node)
      return 1
  length = len(path)
  if length>=2:
    previous_node = path[length -2]

  for node in way[start_node]: 
    size = len(way[node])
    
    if size == 1 or node == previous_node:
      continue
    else:
      
      discontinuity += size-2
      discontinuity_nodes.append(node)
            
      if discontinuity>2:
        continue
      temp = travel(node,end_node)
      if temp == 0:
        continue
      else:
        return 1
  discontinuity += -len(way[start_node])+2
  path.remove(start_node)
  discontinuity_nodes.remove(start_node)
  return 0    

def calculate(node):
  global cost
  #print(cost)
  cost = cost + traffic[node]
  for n in way[node]:
    if n not in path:
      cost = cost + traffic[n]
      if len(way[n]) !=1:
        calculate(n)
             
for i in range(1,N):
    for j in range(i,N+1):
      temp = travel(i,j)
      if len(way[i])>1:
         discontinuity += len(way[i])-1
         discontinuity_nodes.append(i)
      #print(path)
      #print(discontinuity)
      #print("discontinuity nodes:",discontinuity_nodes)
      previous_node = 0
      if discontinuity == 2:
        for k in path:
          cost = cost + traffic[k]
          #print(cost)
       
        option = []
        option.append(cost)
        cost = 0
        
        for k in discontinuity_nodes:
          for node in way[k]:
            #print(node)
            if node not in path:
              #print(node)
              calculate(node)
              option.append(cost)
              cost = 0
        possibilities.append(option)
        
      del path[0:len(path)]
      del discontinuity_nodes[0:len(discontinuity_nodes)]
      discontinuity = 0
#print(possibilities)

maxi = max(possibilities[0])
for chance in possibilities:
  if maxi > max(chance):
    maxi = max(chance)

print(maxi)
