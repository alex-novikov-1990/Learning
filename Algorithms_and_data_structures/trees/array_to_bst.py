def GenerateBBSTArray(a):
    size = len(a)

    if size <= 1:
        return a.copy()

    # check depth
    depth = 0
    depth_pow_2 = 1
    while depth_pow_2 < size:
        depth_pow_2 *= 2
        depth += 1
    if depth_pow_2 - 1 != size:
        raise ValueError("Input array should represent complete binary tree")

    source = sorted(a)
    result = [None] * size
    step = size + 1
    start = (size - 1) // 2
    dst = 0
    while step > 1: # depth
        src = start
        while src < size: # nodes of depth
            result[dst] = source[src]
            src += step
            dst += 1

        start = (start - 1) // 2
        step = step // 2

    return result
