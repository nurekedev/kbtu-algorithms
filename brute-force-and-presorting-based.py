from timer import timing

# Brute-force algorithm (Time complexity: O(n * m))
def intersection_brute_force(A, B):
    C = []
    for a in A:
        for b in B:
            if a == b:
                C.append(a)
    return C

# Presorting-based algorithm (Time complexity: O(n log n + m log m))
def intersection_presorting(A, B):
    A.sort()
    B.sort()
    C = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if not C or C[-1] != A[i]:
                C.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return C

A = [1, 2, 3, 4, 5] * 1000
B = [3, 4, 5, 6, 7] * 1000

@timing
def test_brute_force():
    intersection_brute_force(A, B)

@timing
def test_intersection_presorting():
    intersection_presorting(A, B)

test_brute_force()
test_intersection_presorting()