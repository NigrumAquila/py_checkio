from functools import singledispatch

get_children = singledispatch(lambda _: [])
get_children.register(list)(lambda tree: tree)
get_children.register(dict)(lambda tree: tree.values())

def tree_walker(tree, target):
    return tree == target or sum(tree_walker(child, target) for child in get_children(tree))