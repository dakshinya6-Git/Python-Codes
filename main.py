import heapq
from collections import defaultdict

def get_graph_from_user():
    """Get graph from user input."""
    graph = defaultdict(dict)
    num_vertices = int(input("Enter number of vertices: "))
    
    print("Enter edges (u v weight) or 'done' to finish:")
    while True:
        edge_input = input().strip()
        if edge_input.lower() == 'done':
            break
        
        try:
            u, v, weight = edge_input.split()
            u, v = int(u), int(v)
            weight = int(weight)
            graph[u][v] = weight
            graph[v][u] = weight  # Undirected graph
            print(f"Added edge {u}-{v}: {weight}")
        except:
            print("Invalid input. Use format: u v weight")
    
    return dict(graph)

def prim_mst(graph, start):
    """Prim's algorithm for MST."""
    mst = []
    visited = set()
    pq = [(0, start, None)]  # (cost, node, parent)
    
    while pq:
        cost, u, parent = heapq.heappop(pq)
        
        if u in visited:
            continue
            
        visited.add(u)
        if parent is not None:
            mst.append((parent, u, cost))
        
        for v, weight in graph.get(u, {}).items():
            if v not in visited:
                heapq.heappush(pq, (weight, v, u))
    
    return mst

# Main execution
if __name__ == "__main__":
    graph = get_graph_from_user()
    
    start_vertex = int(input("Enter starting vertex: "))
    mst = prim_mst(graph, start_vertex)
    
    print("\nMinimum Spanning Tree edges:")
    total_cost = 0
    for u, v, w in mst:
        print(f"{u} — {v} (weight: {w})")
        total_cost += w
    
    print(f"\nTotal MST cost: {total_cost}")
