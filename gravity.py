class Node(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.child = set()


def solution(values, edges, queries):
    answer = []
    nodes = []
    i = 1
    for value in values:
        nodes.append(Node(i, value))
        i += 1
    '''for node in nodes:
        print(node.key, node.data)'''



solution([1,10,100,1000,10000], [[1,2],[1,3],[2,4],[2,5]],
         [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]])
