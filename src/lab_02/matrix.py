def transpose(l):
    new_l = []
    if len(l) == 0:
        return new_l
    for i in range(len(l)-1):
        if len(l[i]) != len(l[i+1]):
            raise TypeError
    if len(l) > len(l[0]):
        for i in l:
            for j in i:
                new_l.append(j)
    elif len(l) < len(l[0]):
        for i in l:
            for j in i:
                new_l.append([j])
    elif len(l) == len(l[0]):
        for i in range(len(l)):
            new = []
            for j in range(len(l)):
                new.append(l[j][i])
            new_l.append(new)
                
    return new_l

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))



def row_sums(l):
    new_l = []
    if len(l) == 0:
        return new_l
    for i in range(len(l)-1):
        if len(l[i]) != len(l[i+1]):
            raise TypeError
    for i in l:
        new_l.append(sum(i))
    return new_l

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

def col_sums(l):
    new_l = []
    if len(l) == 0:
        return new_l
    for i in range(len(l)-1):
        if len(l[i]) != len(l[i+1]):
            raise TypeError
    for i in range(len(l)-1):
        for j in range(len(l[0])):
            new_l.append(l[i][j]+l[i+1][j])
    return new_l

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
