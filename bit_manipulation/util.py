def count_bit(i):
    count = 0

    while i != 0:
        if i & 1:
            count += 1
        i = i >> 1

    return count


def xor(i, j):
    return ~(i & j) & (i | j)