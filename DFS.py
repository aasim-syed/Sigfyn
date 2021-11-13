#DFS:
#DFS-EXPLANATION:
#Backtracking is used in Depth-First Search, which is a recursive method.
#It entails searching all of the nodes thoroughly, moving forward if possible and backtracking if not.
#When you are travelling ahead and there are no more nodes along the current path, you retreat on an equivalent path to find nodes to traverse. 
#All of the nodes on the current path will be visited until all of the unvisited nodes have been travelled, at which point new paths will be chosen.



#DFS-PESUDO-CODE:
#DFS(G, u)
#    u.visited = true
#    for each v ∈ G.Adj[u]
#        if v.visited == false
#           DFS(G,v)   
#init() {
#    For each u ∈ G
#        u.visited = false
#     For each u ∈ G
#       DFS(G, u)
#}

# Using dictionary to sort it.
graph = {
  '21' : ['23','27'],
  '31' : ['82', '54'],
  '56' : ['658'],
  '45' : [],
  '443' : ['24'],
  '212' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
