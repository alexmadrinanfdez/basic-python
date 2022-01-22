from collections import deque

# alternative definition of the graph is to define the nodes
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.neighbors = []

class Graph:
    def __init__(self, edge_lst=None):
        self.n_edges = 0
        self.adj_lst = {}
        # build the graph from a list of edges
        if edge_lst:
            for src, dst in edge_lst:
                if src in self.adj_lst:
                    self.adj_lst[src].append(dst)
                else:
                    if dst:
                        self.adj_lst[src] = [dst]
                    # isolated node
                    else:
                        self.adj_lst[src] = []
                        continue
                self.n_edges += 1
                if dst not in self.adj_lst:
                    self.adj_lst[dst] = []
    
    def add_edge(self, edge):
        src, dst = edge
        if src in self.adj_lst:
            self.adj_lst[src].append(dst)
        else:
            if dst:
                self.adj_lst[src] = [dst]
            # isolated node
            else:
                self.adj_lst[src] = []
                return
        self.n_edges += 1
        if dst not in self.adj_lst:
            self.adj_lst[dst] = []
    
    def are_neighbours(self, one, two):
        for neighbour in self.adj_lst[one]:
            if neighbour == two:
                return True
        for neighbour in self.adj_lst[two]:
            if neighbour == one:
                return True
        return False
    
    def is_path(self, source, target, method="bfs"):
        if method == "bfs":
            to_visit = deque()
        elif method == "dfs":
            to_visit = list()
        else:
            raise ValueError("Choose a valid method to traverse the graph.")
        
        visited = set() # to avoid revisiting nodes
        to_visit.append(source)
        while to_visit:
            # get next node
            if method == "bfs":
                curr = to_visit.popleft()
            elif method == "dfs":
                curr = to_visit.pop()
            # check the node and add neighbours
            if curr not in visited:
                if curr == target:
                    return True
                visited.add(curr)
                for neighbour in self.adj_lst[curr]:
                    to_visit.append(neighbour)
        # if never found is not reachable
        return False

    def _dfs_path(self, source, path, visited):
        if source in path:
            return True
        if source in visited:
            return False
        path.append(source)
        visited.add(source)
        for neighbour in self.adj_lst[source]:
            # not considered a cycle
            if neighbour == source:
                continue
            if self._dfs_path(neighbour, path, visited):
                return True
        # if never found there is no cycle
        return False


    def has_cycle(self):
        visited = set()
        for node in self.adj_lst.keys():
            # visited nodes remain, but the path is different
            if self._dfs_path(node, list(), visited):
                return True
        return False

if __name__ == "__main__":
    letters = [
        ('A', 'B'), ('B', 'A'), ('C', 'B'),
        ('C', 'D'), ('D', 'C'), ('F', None)
    ]

    graph = Graph(letters)
    graph.add_edge(('C', 'F'))

    assert graph.n_edges == 6
    assert graph.are_neighbours('B', 'C')
    assert not graph.is_path('A', 'D')
    assert graph.is_path('D', 'A', method="bfs")
    assert graph.is_path('D', 'A', method="dfs")

    assert graph.has_cycle()

    letters = [('A', 'B'), ('B', 'C'), ('A', 'A')]
    graph = Graph(letters)
    assert not graph.has_cycle()
    graph.add_edge(('C', 'A'))
    assert graph.has_cycle()