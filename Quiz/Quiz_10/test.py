def permutations(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

a=permutations(list(range(10)))
b=list(a)
print(len(b))
