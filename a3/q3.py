import sys
import nltk
from nltk.corpus import wordnet as wn

def get_leaves(root):
    children = root.hyponyms()
    if not children:
        # leaf
        return (0, 0, root, root)
    else:
        max_depth = 0
        min_depth = sys.maxint
        ex_min_depth = None
        ex_max_depth = None
        for child in children:
            (child_min_depth, child_max_depth, child_ex_min_depth, child_ex_max_depth) = get_leaves(child)
            if child_max_depth >= max_depth:
                ex_max_depth = child_ex_max_depth
            if child_min_depth < min_depth:
                ex_min_depth = child_ex_min_depth
            max_depth = max(max_depth, child_max_depth)
            min_depth = min(min_depth, child_min_depth)
        return (1 + min_depth, 1 + max_depth, ex_min_depth, ex_max_depth)

if __name__ == '__main__':
    root = wn.synset('entity.n.01')
    (min_leaf_depth, max_leaf_depth, min_leaf_ex, max_leaf_ex) = get_leaves(root)
    print("Min leaf depth: %d" % min_leaf_depth)
    print("Example of leaf at min depth: %s" % min_leaf_ex)
    print("Max leaf depth: %d" % max_leaf_depth)
    print("Example of leaf at max depth: %s" % max_leaf_ex)
