class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = False
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        current_node.count += 1

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.data = True

    def search(self, string):
        current_node = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            elif char == "?":
                break
            else:
                return 0
        count = current_node.count

        return count


def solution(words, queries):
    answer = []
    trie_dic = dict()

    for word in words:
        l = len(word)
        if l not in trie_dic.keys():
            trie_dic[l] = Trie()
            trie_dic[-l] = Trie()
        trie_dic[l].insert(word)
        trie_dic[-l].insert(word[::-1])

    for query in queries:
        l = len(query)
        if l not in trie_dic.keys():
            answer.append(0)
            continue
        if query[-1] == "?":
            answer.append(trie_dic[l].search(query))
        else:
            answer.append(trie_dic[-l].search(query[::-1]))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
