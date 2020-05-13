def earliest_ancestor(ancestors, starting_node):
    # * --------------- GRABBING ALL OF THE VERTEXES WITH PARENTS -------------------------
    # End Result --> {3: [1, 2], 6: [3, 5], 7: [5], 5: [4], 8: [4, 11], 9: [8], 1: [10]}
    # [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    childs = dict()
    # parent, child
    for parent, child in ancestors:
        # if child is in the dict()
        if child in childs:
            # if child is in the dict() it has more parents. Adds the other parents
            childs[child].append(parent)
        # if the child is not in the dict()
        else:
            # adds the child and its parent into the dict() like this {child: [parent]}
            childs[child] = [parent]
    if starting_node not in childs:
        return -1
    # * -------------------------------------------------------------------------------------------------------------------
    # [[child]]
    g = [[starting_node]]
    # [child]
    for children in g:
        parents = []
        # child
        for child in children:
            # if child is in the dict()
            if child in childs:
                # adds the childs parents to the parents array
                parents.extend(childs[child])
        # if parents array is not empty
        if len(parents) >= 1:
            # adds the parents array to the end of the g array
            g.append(parents)
        # if parents array is empty
        else:
            break
    # if there is a tie for the earliest, returns the lowest number, otherwise returns the last number in the g array which is the furthest away vertex
    return min(g[-1])

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)
