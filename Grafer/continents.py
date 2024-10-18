from collections import defaultdict
import graphviz



def build_graph(file):
    V = set()
    E = defaultdict(set)
    
    with open(file) as f:
        for line in f:
            line = line.strip().split(" ")
            v = line[0]
            
            if len(line) == 1:
                V.add(v)
                
                E[v] = set()
            else:
                u = line[1]
                
                V.add(v)
                V.add(u)

                E[v].add(u)
                E[u].add(v)
                
    return V, E



def BFS_from_node(G, s, visited):
    V, E = G
    
    visited.add(s)
    queue = [s]
    result = []
    
    while len(queue) != 0:
        v = queue.pop(0)
        result.append(v)
        
        for u in E[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    
    return result



def find_continents(G):
    V, E = G
    
    visited = set()
    
    continents = []
        
    for v in V:
        if v not in visited:
            continent = BFS_from_node(G, v, visited)
            continents.append(continent)
    
    return continents
    


def draw_graph(G):
    V, E = G
    dot = graphviz.Graph()
    seen_edges = set()
    
    for v in V:
        dot.node(v)
        
        for u in E[v]:
            if (v, u) in seen_edges:
                continue
            seen_edges.add((u, v))
            dot.edge(v, u)
    
    dot.render("countries", format="svg")
    
        

def main():
    G = build_graph("countries.txt")
    
    continents = find_continents(G)
    print(continents)
    
    draw_graph(G)

main()