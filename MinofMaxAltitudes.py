#Min of max altitudes


#Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

#Don't include the first or final entry. You can only move either down or right at any point in time.
#from itertools import permutations

a=[[1, 2, 3],[4, 5, 1]]
rows=len(a)
cols=len(a[0])

routepath="r"*(cols-1)+"d"*(rows-1)
routes=set(permutations(list(routepath)))

fin=[]
for i in routes:
    scores=[]
    curr=[0,0]
    i=i[:-1]
    for k in i:
        if k=='r':
            curr=[curr[0],curr[1]+1]
            scores.append(a[curr[0]][curr[1]])
        else:
            curr=[curr[0]+1,curr[1]]
            scores.append(a[curr[0]][curr[1]])
    fin.append(min(scores))
print(max(fin))
