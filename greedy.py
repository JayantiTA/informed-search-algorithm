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

def greedy_search(source, target):
  visited = {}
  route = []
  
  for key in dict:
    visited[key] = False
  
  visited[source] = True
  p_queue = PriorityQueue()
  p_queue.put((dict[source], source))
  
  while p_queue.empty() == False:
    current_node = p_queue.get()[1]
    route.append(current_node)

    if current_node == target:
      break

    for node in graph[current_node]:
      if visited[node] == False:
        visited[node] = True
        p_queue.put((dict[node], node))

  print("route: ", ' -> '.join(route))


def addedge(x, y):
  graph[x].append(y)
  graph[y].append(x)

addedge("Bandarlampung", "Jakarta")
addedge("Jakarta", "Bogor")
addedge("Jakarta", "Cirebon")
addedge("Bogor", "Bandung")
addedge("Cirebon", "Bandung")
addedge("Cirebon", "Cilacap")
addedge("Cirebon", "Purwokerto")
addedge("Cirebon", "Semarang")
addedge("Bandung", "Tasikmalaya")
addedge("Tasikmalaya", "Cilacap")
addedge("Cilacap", "Purwokerto")
addedge("Purwokerto", "Yogyakarta")
addedge("Semarang", "Yogyakarta")

source = "Bandarlampung"
target = "Yogyakarta"
greedy_search(source, target)
