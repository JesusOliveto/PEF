def suma_cython(int n):
    cdef int total = 0
    cdef int i
    for i in range(n):
        total += i
    return total


