def sort_merge(a, b):
    """
    it takes 2 sorted in increase order arrays and return a sorted in increased order array that consists of
    elements of this 2 arrays
    :param a: array sorted in increased order
    :param b:  array sorted in increased order
    :return: array that consist of elements of both of arrays with are sorted in increase order
    """
    if not isinstance(a, list):
        raise TypeError('a argument must be list ')
    if not isinstance(b, list):
        raise TypeError('b argument must be list ')
    if not a:
        return b
    if not b:
        return a
    res = []
    a_i = 0
    b_i = 0
    for i in range(len(a) + len(b)):
        if a_i >= len(a):
            append_a = False
        elif b_i >= len(b):
            append_a = True
        else:
            append_a = a[a_i] < b[b_i]
        if append_a:
            res.append(a[a_i])
            a_i += 1
        else:
            res.append(b[b_i])
            b_i += 1
    return res


def iter_sort_merge(a, b):
    """
    it takes 2 iterators on sorted in increase order arrays and return a sorted in increased order array that consists of
    elements of this 2 iterable
    :param a: array sorted in increased order
    :param b:  array sorted in increased order
    :return: generator that consist of elements of both of arrays with are sorted in increase order
    """
    el_a = a.__next__()
    el_b = b.__next__()
    while True:
        if el_a is None:
            append_a = False
        elif el_b is None:
            append_a = True
        else:
            append_a = el_a < el_b
        if append_a:
            yield el_a
            el_a = a.__next__()
        else:
            yield el_b
            el_b = b.__next__()


def merge_sort(a):
    """
    implemetation of algorithm mere sort
    works with int values
    :param a: iterator on a collection that need to be sorted
    :return: list of sorted int values
    """
    res = [a.__next__()]
    tmp = []
    for i in a:
        if len(tmp) == len(res):
            res1 = sort_merge(res, tmp)
            # clear memory
            del res
            del tmp
            # create link and new obj for temp
            res = res1
            tmp = []
        tmp1 = sort_merge(tmp, [i])
        del tmp
        tmp = tmp1
    if tmp:
        res1 = sort_merge(res, tmp)
    # clear memory
    del res
    del tmp
    return res1
