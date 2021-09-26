import time
import sys
sys.setrecursionlimit(10000)

class Node(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.child = list()


def sum_from_node(nodes, num):
    ans = nodes[num].data
    if len(nodes[num].child) == 0:
        return nodes[num].data
    else:
        for i in nodes[num].child:
            ans += sum_from_node(nodes, i)
    return ans


def sec_query(parent, nodes, num, w):
    if nodes[num].key == 1:
        nodes[num].data = w
    else:
        temp = nodes[parent[num]].data
        nodes[num].data = temp
        sec_query(parent, nodes, parent[num], w)


def solution(values, edges, queries):
    answer = []
    nodes = [Node(0,0)]
    parent = [0 for _ in range(len(values)+1)]
    i = 1
    for value in values:
        nodes.append(Node(i, value))
        i += 1
    '''for node in nodes:
        print(node.key, node.data)'''
    for edge in edges:
        nodes[edge[0]].child.append(edge[1])
        parent[edge[1]] = edge[0]

    for query in queries:
        if query[1] == -1:
            answer.append(sum_from_node(nodes, query[0]))
        else:
            sec_query(parent, nodes, query[0], query[1])

    return answer

start = time.time()
print(solution([1,10,100,1000,10000], [[1,2],[1,3],[2,4],[2,5]],
         [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]))
print(time.time()-start)
