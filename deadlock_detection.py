import networkx as nx

class WaitForGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, p1, p2):
        self.graph.add_edge(p1, p2)

    def detect_deadlock(self):
        try:
            cycle = nx.find_cycle(self.graph)
            return True, cycle
        except:
            return False, None
