def combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for c in combinations(rest_arr, n - 1):
            result.append([elem, *c])

    return result


arr = combinations([1, 2, 3, 4], 2)
print(arr)


def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, e in enumerate(arr):
        for p in permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[e] + p]

    return result


print(permutations([1, 2, 3, 4], 2))

