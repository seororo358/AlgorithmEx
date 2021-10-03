from collections import deque


class Node(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.child = list()

# 1번째 쿼리: 노드를 루트로 갖는 서브트리데이터 총합
def sum_from_node(nodes, num):
    ans = nodes[num].data
    if len(nodes[num].child) == 0:
        return nodes[num].data
    else:
        q = deque()
        q.extend(nodes[num].child)
        while q:
            ans += nodes[q[0]].data
            q.extend(nodes[q.popleft()].child)

    return ans

# 2번째 쿼리: 순차적으로 부모노드값 복사
def sec_query(parent, nodes, num, w):
    if nodes[num].key == 1:
        nodes[num].data = w
    else:
        current_node = num
        while current_node != 1:
            nodes[current_node].data = nodes[parent[current_node]].data
            current_node = parent[current_node]
        nodes[current_node].data = w


def solution(values, edges, queries):
    answer = []
    nodes = [Node(0, 0)]
    parent = [0 for _ in range(len(values)+1)]
    i = 1
    for value in values:
        nodes.append(Node(i, value))
        i += 1
    '''for node in nodes:
        print(node.key, node.data)'''
    for edge in edges:
        ma = max(edge)
        mi = min(edge)
        nodes[mi].child.append(ma)
        parent[ma] = mi

    for query in queries:
        if query[1] == -1:
            answer.append(sum_from_node(nodes, query[0]))
        else:
            sec_query(parent, nodes, query[0], query[1])

    return answer



print(solution([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],
               [[10, 11], [13, 11], [12, 10], [10, 9], [8, 9], [1, 2], [2, 4], [2, 3], [5, 3], [6, 5], [5, 8], [7, 5]],
         [[7,8192],[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1], [7, -1], [8, -1], [9, -1], [10, -1], [11, -1], [12, -1], [13, -1]]))

