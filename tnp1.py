#n=Queen's
def safe(l,r,c):
    for i in range(0,c+1):
        if l[r][i]!=0:
            return False
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        if l[i][j]!=0:
            return False
    for i,j in zip(range(r,4),range(c,-1,-1)):
        if l[i][j]!=0:
            return False
    return True

def matrix(l,c):
    if c>=4:
        return True
    for i in range(0,4):
        l[i][c]=1
        if safe(l,i,c)==True:
            return  True
            if matrix(l,c+1)==True:
                return  True
        l[i][c]=0
    return False

l=[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
if (matrix(l,0)==True):
    for i in range(0,4):
        for j in range(0,4):
            print(l[i][j],end=" ")
        print()
else:
    print("No solution")