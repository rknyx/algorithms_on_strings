# python3
import sys


class Node:
    def __init__(self, next=None, symbol=None, is_complete_pattern=False):
        self.next = next if next is not None else {}
        self.symbol = symbol
        self.is_complete_pattern = is_complete_pattern

    def add_next(self, next_node):
        self.next[next_node.symbol] = next_node
        return next_node


def build_trie(patterns):
    root_node = Node(symbol=-1)
    for pattern in patterns:
        curr = root_node
        for symbol in pattern:
            curr = curr.next[symbol] if symbol in curr.next else curr.add_next(Node(symbol=symbol))
        curr.is_complete_pattern = curr.next
    return root_node


def solve(text, root_node):
    result = set()
    text_length = len(text)
    for start_num in range(text_length):
        current_node = root_node
        for symbol in text[start_num:]:
            if symbol in current_node.next:
                current_node = current_node.next[symbol]
                if not current_node.next or current_node.is_complete_pattern:
                    result.add(start_num)
            else:
                break
    return sorted(result)

test_inpu1 = """AAAAAA
2
A
AA
"""

if __name__ == '__main__':
    # all_input = test_inpu1.split()
    all_input = sys.stdin.read().split()
    text = all_input[0].strip()
    n = int(all_input[1].strip())
    patterns = [i.strip() for i in all_input[2:]]
    trie =  build_trie(patterns)
    ans = solve(text, trie)

    sys.stdout.write (' '.join (map (str, ans)) + '\n')
