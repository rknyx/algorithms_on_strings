#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

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
test_input1 = """
1
ATA
"""
test_input2 = """
3
AT
AG
AC
"""
if __name__ == '__main__':
    inp = sys.stdin.read()
    # inp = test_input1
    patterns = inp.split()[1:]
    tree = build_trie(patterns)
    print("\n".join(["%s->%s:%s" % (num, node[key], key) for (num, node) in enumerate(tree) for key in node]))
