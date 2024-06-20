def dfs(graph,visited,stack,element):
    if visited[element]==False:
        stack.append(element)
        visited[element]=True
    else:
        return
    for i in graph[element]:
        dfs(graph,visited,stack,i[1])
    print(stack.pop())

graph={1:[(1,2,0),(1,3,0)],2:[(2,1,0),(2,7,0)],3:[(3,1,0),(3,5,0),(3,6,0)],4:[(4,7,0),(4,8,0)],5:[(5,3,0),(5,7,0)],6:[(6,3,0),(6,8,0)],7:
      [(7,2,0),(7,4,0),(7,5,0)],8:[(8,4,0),(8,6,0)]}
visited={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,}
stack=[]
for i in graph:
    dfs(graph,visited,stack,i)
