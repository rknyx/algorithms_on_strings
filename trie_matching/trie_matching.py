# python3
import sys

# NA = -1
#
# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4


def build_trie(patterns):
    tree = [{}]
    root_node = 0
    global_iterator = 1
    for pattern in patterns:
        curr_node = root_node
        for i in range(len(pattern)):
            symbol = pattern[i]
            if symbol in tree[curr_node]:
                curr_node = tree[curr_node][symbol]
            else:
                tree[curr_node][symbol] = global_iterator
                curr_node = global_iterator
                global_iterator += 1
                tree.append({})
    return tree

def solve(text, trie):
    result = []
    text_length = len(text)
    for start_num in range(text_length):
        current_node = 0
        for symbol in text[start_num:]:
            if symbol in trie[current_node]:
                current_node = trie[current_node][symbol]
                if not trie[current_node]:
                    result.append(start_num)
            else:
                break
    return sorted(result)

test_inpu1 = """AAA
1
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
