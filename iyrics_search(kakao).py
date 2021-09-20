class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = len(string)

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            elif char == "?":
                break
            else:
                return 0
        count = searching(current_node, len(string))
        return count


def searching(node, length):
    if node.data == length:
        return 1
    else:
        count = 0
        for N in node.children.keys():
            count += searching(node.children[N], length)

        return count


def solution(words, queries):
    answer = []
    trie = Trie()
    trie_back = Trie()
    for word in words:
        trie.insert(word)
        reversing = word[::-1]
        trie_back.insert(reversing)

    for query in queries:
        if query[-1] == "?":
            answer.append(trie.search(query))
        else:
            reversing = query[::-1]
            answer.append(trie_back.search(reversing))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
