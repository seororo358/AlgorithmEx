class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = False
        self.count = 0
        self.depth = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        cur_node.count += 1
        depth = 1
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
            cur_node.depth = depth
            cur_node.count += 1
            depth += 1
        cur_node.data = True


def search_all(node):
    answer = 0
    if node.count == 1:
        return node.depth
    else:
        if node.data:
            answer += node.depth
        for n in node.children.keys():
            answer += search_all(node.children[n])

    return answer


def solution(words):
    answer = 0
    trie = Trie()

    for word in words:
        trie.insert(word)

    answer += search_all(trie.head)

    return answer


print(solution(["word", "war", "warrior", "world"]))
