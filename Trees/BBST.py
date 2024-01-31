def GenerateBBSTArray(a):
    sorted_array = sorted(a)
    depth = _depth_from_len(len(sorted_array))
    tree = [None] * _len_from_depth(depth)
    _fill_subtree(sorted_array, 0, tree)
    return tree


def _depth_from_len(n):
    m = 1
    d = 0
    while m < n + 1:
        m *= 2
        d += 1
    return d - 1


def _len_from_depth(d):
    return 2 ** (d + 1) - 1


def _fill_subtree(sorted_array, start, tree):
    if sorted_array == []:
        return
    mid_index = len(sorted_array) // 2
    tree[start] = sorted_array[mid_index]
    left = 2 * start + 1
    _fill_subtree(sorted_array[:mid_index], left, tree)
    right = 2 * start + 2
    _fill_subtree(sorted_array[mid_index + 1:], right, tree)
