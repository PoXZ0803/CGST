import random
from collections import defaultdict

def maxWeightedClique(ordering, graph):
    random.seed()
    weights = {i: random.randint(1, len(ordering)) for i in range(len(ordering))}
    max_weight_sum = 1
    clique = []
    S = [0] * len(ordering)
    idx = {ordering[i]: i for i in range(len(ordering))}

    for i in range(len(ordering)):
        current_weight = 0
        v = ordering[i]
        X = [adj_v for adj_v in graph[v] if idx[v] < idx[adj_v]]
        
        if graph[v]:
            if X:
                u = min(X, key=lambda x: idx[x])
                for adj_v in X:
                    current_weight += weights[adj_v]
                vertex_wt = weights[u]
                S[u] = max(S[u], current_weight - vertex_wt)
                if S[v] < current_weight:
                    current_weight += weights[v]
                    if max_weight_sum < current_weight:
                        max_weight_sum = current_weight
                        X.append(v)
                        clique = X[:]
    
    print("THE MAXIMUM WEIGHTED CLIQUE SUM:", max_weight_sum)
    print("THE MAXIMUM WEIGHTED CLIQUE CONSISTS OF THE FOLLOWING VERTICES:")
    print("VERTEX : WEIGHT")
    for vertex in clique:
        print(f"{vertex} : {weights[vertex]}")


def maxIndependentSet(ordering, graph):
    visited = [False] * len(ordering)
    independentSet = {}
    cliqueCover = []
    idx = {ordering[i]: i for i in range(len(ordering))}

    for v in ordering:
        if not visited[v]:
            X = [adj_v for adj_v in graph[v] if idx[v] < idx[adj_v]]
            
            if not graph[v]:
                clique = [v]
                cliqueCover.append(clique)
                if v not in independentSet:
                    independentSet[v] = 1
            else:
                for adj_v in X:
                    visited[adj_v] = True
                if v not in independentSet:
                    independentSet[v] = 1
                X.append(v)
                clique = X[:]
                cliqueCover.append(clique)
    
    print("THE MAXIMUM INDEPENDENT SET CONSISTS OF THE FOLLOWING VERTICES:", ' '.join(map(str, independentSet.keys())))
    print("THE MINIMUM CLIQUE COVER:", len(cliqueCover))


def maxclique(ordering, graph):
    chromatic_number = 1
    clique = []
    S = [0] * len(ordering)
    idx = {ordering[i]: i for i in range(len(ordering))}

    for v in ordering:
        X = [adj_v for adj_v in graph[v] if idx[v] < idx[adj_v]]
        
        if X:
            u = min(X, key=lambda x: idx[x])
            S[u] = max(S[u], len(X) - 1)
            if S[v] < len(X):
                new_chromatic_number = max(chromatic_number, len(X) + 1)
                if new_chromatic_number > chromatic_number:
                    clique = X[:]
                    clique.append(v)
                    chromatic_number = new_chromatic_number

    print("THE MAXIMUM CLIQUE CONSISTS OF THE FOLLOWING VERTICES:", ' '.join(map(str, clique)))
    print("CHROMATIC NUMBER OF THE GRAPH:", chromatic_number)


def DIFF(A2, Adj_v, n):
    freq = [0] * (n + 1)
    for v in Adj_v:
        freq[v] = 1
    for v in A2:
        if freq[v] == 0:
            return False
    return True


def checkPerfectEliminationOrdering(ordering, graph):
    A = defaultdict(list)
    idx = {ordering[i]: i for i in range(len(ordering))}

    for i in range(len(ordering) - 1):
        v = ordering[i]
        X = [adj_v for adj_v in graph[v] if idx[v] < idx[adj_v]]
        
        if X:
            u = min(X, key=lambda x: idx[x])
            for x in X:
                if x != u:
                    A[u].append(x)

        A2 = A[v]
        Adj_v = graph[v]
        if not DIFF(A2, Adj_v, len(ordering)):
            return False
    return True


def MCS(graph, vertices, edges):
    node_store = defaultdict(lambda: defaultdict(int))
    for i in range(vertices):
        node_store[0][i] += 1
    label_store = {i: 0 for i in range(vertices)}
    ordering = []
    label_count = {0: vertices}
    visited = {}

    for m in range(vertices - 1, -1, -1):
        current_label = max(label_count)
        label_count[current_label] -= 1
        if label_count[current_label] == 0:
            del label_count[current_label]
        
        current_vertex = next(iter(node_store[current_label]))
        ordering.append(current_vertex)
        visited[current_vertex] = 1
        del node_store[current_label][current_vertex]
        
        for adj_v in graph[current_vertex]:
            if adj_v not in visited:
                adj_label = label_store[adj_v]
                new_label = adj_label + 1
                label_store[adj_v] = new_label
                node_store[adj_label].pop(adj_v, None)
                if adj_label in label_count:
                    label_count[adj_label] -= 1
                    if label_count[adj_label] == 0:
                        del label_count[adj_label]
                node_store[new_label][adj_v] += 1
                label_count[new_label] += 1
    
    ordering.reverse()
    return ordering


def LEXBFS(graph, vertices, edges):
    node_store = defaultdict(lambda: defaultdict(int))
    for i in range(vertices):
        node_store[""][i] += 1
    label_store = {i: "" for i in range(vertices)}
    ordering = []
    label_count = {"": vertices}
    visited = {}

    for m in range(vertices - 1, -1, -1):
        current_label = max(label_count)
        label_count[current_label] -= 1
        if label_count[current_label] == 0:
            del label_count[current_label]
        
        current_vertex = next(iter(node_store[current_label]))
        ordering.append(current_vertex)
        visited[current_vertex] = 1
        del node_store[current_label][current_vertex]
        
        for adj_v in graph[current_vertex]:
            if adj_v not in visited:
                adj_label = label_store[adj_v]
                new_label = adj_label + '1'
                label_store[adj_v] = new_label
                node_store[adj_label].pop(adj_v, None)
                if adj_label in label_count:
                    label_count[adj_label] -= 1
                    if label_count[adj_label] == 0:
                        del label_count[adj_label]
                node_store[new_label][adj_v] += 1
                label_count[new_label] += 1

    ordering.reverse()
    return ordering


def main():
    vertices = int(input("ENTER THE NUMBER OF VERTICES: "))
    edges = int(input("ENTER THE NUMBER OF EDGES: "))

    graph = defaultdict(list)
    print("ENTER ALL THE VERTEX PAIRS FOR EDGES:")
    for _ in range(edges):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    ordering_lexbfs = LEXBFS(graph, vertices, edges)
    ordering_mcs = MCS(graph, vertices, edges)

    print("LEXBFS ORDERING:", ' '.join(map(str, ordering_lexbfs)))
    print("MCS ORDERING:", ' '.join(map(str, ordering_mcs)))

    if checkPerfectEliminationOrdering(ordering_lexbfs, graph):
        print("THE GIVEN INPUT GRAPH IS A CHORDAL GRAPH")
        maxclique(ordering_lexbfs, graph)
        maxIndependentSet(ordering_lexbfs, graph)
        maxWeightedClique(ordering_lexbfs, graph)
    else:
        print("THE INPUT GRAPH IS NOT A CHORDAL GRAPH")

main()