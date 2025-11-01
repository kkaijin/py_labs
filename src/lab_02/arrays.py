
def min_max(l):
    t = []
    Min = 10**9
    Max = -10**9
    for i in l:
        if i > Max:
            Max = i
        if i < Min:
            Min = i
        t.append(i)
    t = tuple(t)
    if len(l) == 0:
        raise TypeError
    else:
        return (Min,Max)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([1.5, 2, 2.0, -3.1]))  
print(min_max([]))
  

def unique_sorted(l):
    if len(l) == 0:
        return l
    l = sorted(set(l))
    l = list(l)
    
    return l
# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
# print(unique_sorted([])) 

def flatten(l):
    for i in l:
        if type(i) not in [list,tuple]:
            raise TypeError
    new_l = [j for i in l for j in i]
    return new_l

# print(flatten([[1, 2], [3, 4]]))
# print(flatten([[1, 2], (3, 4, 5)]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"])) 
    
  


