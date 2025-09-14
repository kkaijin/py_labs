N = input('in_1: ')
N = int(N)
people = []
t = 0
fa = 0
for i in range(N):
    s,n,a,f = input(f'in_{i+2}: ').split()
    if f == 'True' or f == 'true':
        t += 1
    else:
        fa += 1
    people.append([s,n,a,f])
#print(*[f'in_{i+2}: {people[i]}' for i in range(len(people))], sep='\n')
print('out:',t,fa)