# python3

""" 
suffix_tree.py

A string Text is inputted ending with a “$” symbol.The strings labeling the edges of 
SuffixTree(Text) in any order.

"""


from collections import deque


class BuildSuffixTree(object):
    """Build suffix tree without suffix links"""

    class MakeNode(object):
        """Creates a tree node"""

        def __init__(self, label):
            self.label = label
            self.outgoing = {}

    def __init__(self, suffix):
        """Build tree without suffix links"""
        self.root = self.MakeNode(None)
        self.root.outgoing[suffix[0]] = self.MakeNode(suffix)
        for i in range(1, len(suffix)):
            cur = self.root
            j = i
            while j < len(suffix):
                if suffix[j] in cur.outgoing:
                    child = cur.outgoing[suffix[j]]
                    label = child.label
                    k = j + 1
                    while k - j < len(label) and suffix[k] == label[k - j]:
                        k += 1
                    if k - j == len(label):
                        cur = child
                        j = k
                    else:
                        existing_char, new_char = label[k - j], suffix[k]
                        mid = self.MakeNode(label[: k - j])
                        mid.outgoing[new_char] = self.MakeNode(suffix[k:])
                        child.label = label[k - j :]
                        mid.outgoing[existing_char] = child
                        cur.outgoing[suffix[j]] = mid
                else:
                    cur.outgoing[suffix[j]] = self.MakeNode(suffix[j:])

    def display_tree(self):
        """Print the tree"""
        queue = deque()
        queue.append(self.root)
        while queue:
            _q = queue.popleft()
            if _q != self.root:
                print(_q.label)
            for _, node in _q.outgoing.items():
                queue.append(node)


if __name__ == "__main__":
    text = input()
    suffix_tree = BuildSuffixTree(text)
    suffix_tree.display_tree()
