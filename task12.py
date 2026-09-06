import math
def dot_product(v1,v2):
    return sum(x*y for x,y in zip(v1,v2))
    
def vector_norm(v):
    return math.sqrt(sum(x**2 for x in v))

def scalar_multiply(c,v):
    return [c*x for x in v]

def vector_subtract(v1,v2):
    return [x-y for x,y in zip(v1,v2)]

def matrix_multiply(A,B):
    n=len(A)
    m=len(B[0])
    k=len(B)
    C=[[0.0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j]=sum(A[i][p]*B[p][j] for p in range(k))
    return C

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def identity_matrix(n):
    return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]

def qr_decomposition(A):
    n=len(A)
    cols=[[A[row][col] for row in range(n)] for col in range(n)]
    Q_cols=[]
    R=[[0.0]*n for _ in range(n)]
    for j in range(n):
        v=cols[j][:]

        for i in range(j):
            q_i=Q_cols[i]
            r_ij=dot_product(cols[j],q_i)
            R[i][j]=r_ij
            v=vector_subtract(v,scalar_multiply(r_ij,q_i))

        r_jj=vector_norm(v)

        R[j][j]=r_jj

        if r_jj<1e-12:
            q_j=[0.0]*n

        else:
            q_j=scalar_multiply(1.0/r_jj,v)

        Q_cols.append(q_j)

    Q=[[Q_cols[col][row] for col in range(n)] for row in range(n)]

    return Q,R

def eig(A,max_iterations=1000,tol=1e-10):
    n=len(A)
    Ak=[row[:] for row in A]
    V=identity_matrix(n)
    for _ in range(max_iterations):
        Q,R=qr_decomposition(Ak)
        Ak_next=matrix_multiply(R,Q)
        V=matrix_multiply(V,Q)
        diff=sum(abs(Ak_next[i][j]) for i in range(n) for j in range(i))
        Ak=Ak_next
        if diff<tol:
            break
    eigenvalues=[Ak[i][i] for i in range(n)]
    eigenvectors=[[V[row][col] for row in range(n)] for col in range(n)]
    return eigenvalues,eigenvectors

if __name__=="__main__":
    matrix=[
        [4.0,1.0,1.0],
        [1.0,3.0,0.0],
        [1.0,0.0,2.0]
    ]

    values,vectors=eig(matrix)

    print("Eigenvalues:")

    for i,val in enumerate(values):
        print(f" λ{i+1} = {val:.6f}")

    print("\nCorresponding Eigenvectors (normalized columns):")

    for i,vec in enumerate(vectors):
        formatted_vec=[round(x,6) for x in vec]
        print(f" v{i+1} = {formatted_vec}")

            
            

            

