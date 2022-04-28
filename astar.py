from collections import defaultdict
from queue import PriorityQueue

dict = {
  "Bandarlampung": 629,
  "Jakarta": 446,
  "Bogor": 421,
  "Bandung": 320,
  "Cirebon": 246,
  "Tasikmalaya": 248,
  "Purwokerto": 132,
  "Cilacap": 156,
  "Semarang": 108,
  "Yogyakarta": 0
}

graph = defaultdict(list)

def a_star_search(source, target):
  visited = []
  traced = {}
  route = []
  p_queue = PriorityQueue()
  p_queue.put((dict[source], source, 0, None))
  
  while p_queue.empty() == False:
    current_cost, current_node, prev_cost, prev_node = p_queue.get()

    if current_node not in visited:
      visited.append(current_node)
      traced[current_node] = prev_node
      if current_node == target:
        route.append(current_node)
        print("cost: ", current_cost)
        while prev_node != None:
          route.append(prev_node)
          prev_node = traced[prev_node]
        break

      for node, cost in graph[current_node]:
        total_cost = cost + prev_cost
        p_queue.put((dict[node] + total_cost, node, total_cost, current_node))

  route.reverse()
  return visited, traced, route

def addedge(x, y, cost):
  graph[x].append((y, cost))
  graph[y].append((x, cost))

addedge("Bandarlampung", "Jakarta", 233)
addedge("Jakarta", "Bogor", 56)
addedge("Jakarta", "Cirebon", 219)
addedge("Bogor", "Bandung", 124)
addedge("Cirebon", "Bandung", 129)
addedge("Cirebon", "Cilacap", 170)
addedge("Cirebon", "Purwokerto", 146)
addedge("Cirebon", "Semarang", 234)
addedge("Bandung", "Tasikmalaya", 111)
addedge("Tasikmalaya", "Cilacap", 140)
addedge("Cilacap", "Purwokerto", 50)
addedge("Cilacap", "Yogyakarta", 172)
addedge("Purwokerto", "Yogyakarta", 168)
addedge("Semarang", "Yogyakarta", 130)

source = "Bandarlampung"
target = "Yogyakarta"
visited, traced, route = a_star_search(source, target)

print("\n The visited nodes are:")
print(visited)

print("\n The path followed is:")
print(route)

print("\n The List of previous nodes are:")
print(traced)
