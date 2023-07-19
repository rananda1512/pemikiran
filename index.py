import sys

class Graph(object):
    def __init__(self,nodes,init_graph):
        self.nodes=nodes
        self.graph=self.construct_graph(nodes,init_graph)
    
    def construct_graph(self,nodes,init_graph):
        graph={}
        for node in nodes:
            graph[node]={}
        graph.update(init_graph)
        for node,edges in graph.items():
            for adjacent_node,value in edges.items():
                if graph[adjacent_node].get(node,False)==False:
                    graph[adjacent_node][node]=value
        return graph
    
    def get_nodes(self):
        return self.nodes
    def get_outgoing_edges(self,node):
        connections=[]

        for out_node in self.nodes:
            if self.graph[node].get(out_node,False)!=False:
                connections.append(out_node)
        return connections
    
    def value(self,node1,node2):
        return self.graph[node1][node2]
    
def print_result(previous_nodes,shortest_path,start_node,target_node):
    path=[]
    node=target_node

    while node !=start_node:
        path.append(node)
        node=previous_nodes[node]
    path.append(start_node)
    print("Rute tercepat yang dapat ditempuh adalah {} km. ".format(shortest_path[target_node]))
    print("->".join(reversed(path)))

def dijkstra_algorithm(graph,start_node):
    unvisited_nodes=list(graph.get_nodes())
    shortest_path={}
    previous_nodes={}
    max_value=sys.maxsize

    for node in unvisited_nodes:
        shortest_path[node]=max_value
    
    shortest_path[start_node]=0
    while unvisited_nodes:
        current_min_node=None
        for node in unvisited_nodes:
            if current_min_node==None:
                current_min_node=node
            elif shortest_path[node]<shortest_path[current_min_node]:
                current_min_node=node
        neighbors=graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value=shortest_path[current_min_node] +graph.value(current_min_node,neighbor)
            if tentative_value<shortest_path[neighbor]:
                shortest_path[neighbor]=tentative_value
                previous_nodes[neighbor]=current_min_node
        unvisited_nodes.remove(current_min_node)
    return previous_nodes,shortest_path

ba=(input().split())
nodes=["Minstowe","Cowstone","Oldcastle","Freeham","New North","Bingborough","Donningpool","Highbrook","Wington","Freeham","Old Mere"]

init_graph={}
for node in nodes:
    init_graph[node]={}

init_graph["Minstowe"]["Cowstone"]=3
init_graph["Oldcastle"]["New North"]=5
init_graph["Oldcastle"]["Freeham"]=2
init_graph["Cowstone"]["New North"]=4
init_graph["Cowstone"]["Bingborough"]=6
init_graph["Cowstone"]["Donningpool"]=7
init_graph["Cowstone"]["Highbrook"]=5
init_graph["New North"]["Bingborough"]=3
init_graph["New North"]["Donningpool"]=6
init_graph["New North"]["Wington"]=4
init_graph["New North"]["Highbrook"]=2
init_graph["Freeham"]["Cowstone"]=2
init_graph["Freeham"]["Donningpool"]=3
init_graph["Freeham"]["Wington"]=5
init_graph["Bingborough"]["Donningpool"]=2
init_graph["Bingborough"]["Highbrook"]=1
init_graph["Donningpool"]["Wington"]=4
init_graph["Donningpool"]["Highbrook"]=5
init_graph["Donningpool"]["Old Mere"]=2

graph=Graph(nodes,init_graph)
print(init_graph)
start=input()
end=input()
previous_nodes,shortest_path=dijkstra_algorithm(graph=graph,start_node=start)
print_result(previous_nodes,shortest_path,start_node=start,target_node=end)
