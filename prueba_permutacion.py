def permutations(start, end=[]):
    if len(start) == 0:
        print(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i + 1 :], end + start[i : i + 1])


n = (3,4,5,2)
r = (7,8)
permutations(3,4,5,6)