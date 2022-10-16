def dz_func4(l1,l2):
    assert(len(l1) == len(l2))
    return [i if i==j else -1 for i, j in zip(l1, l2)]

print(dz_func4([1,2,3,4,5],[2,2,4,4,5]))