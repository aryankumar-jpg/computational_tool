import numpy as np

class MatrixWithoutNumPy:
    
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return MatrixWithoutNumPy(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return MatrixWithoutNumPy(result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Columns of first matrix must match rows of second matrix for multiplication.")
        
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) 
                   for j in range(other.cols)] for i in range(self.rows)]
        return MatrixWithoutNumPy(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return MatrixWithoutNumPy(result)

    def display(self):
        for row in self.data:
            print(row)


class MatrixWithNumPy:
    
    def __init__(self, data):
        self.matrix = np.array(data)

    def add(self, other):
        return MatrixWithNumPy((self.matrix + other.matrix).tolist())

    def subtract(self, other):
        return MatrixWithNumPy((self.matrix - other.matrix).tolist())

    def multiply(self, other):
        return MatrixWithNumPy((np.dot(self.matrix, other.matrix)).tolist())

    def transpose(self):
        return MatrixWithNumPy((self.matrix.T).tolist())

    def display(self):
        print(self.matrix)

if __name__ == "__main__":
    print("=== 1. WITHOUT NUMPY ===")
    m1_list = [[1, 2], [3, 4]]
    m2_list = [[5, 6], [7, 8]]
    
    mat1_wn = MatrixWithoutNumPy(m1_list)
    mat2_wn = MatrixWithoutNumPy(m2_list)

    print("Matrix 1:")
    mat1_wn.display()
    
    print("\nMatrix 2:")
    mat2_wn.display()

    print("\nAddition (Matrix 1 + Matrix 2):")
    mat1_wn.add(mat2_wn).display()

    print("\nSubtraction (Matrix 1 - Matrix 2):")
    mat1_wn.subtract(mat2_wn).display()

    print("\nMultiplication (Matrix 1 * Matrix 2):")
    mat1_wn.multiply(mat2_wn).display()

    print("\nTranspose of Matrix 1:")
    mat1_wn.transpose().display()

    print("\n" + "="*30 + "\n")

    print("=== 2. WITH NUMPY ===")
    mat1_np = MatrixWithNumPy(m1_list)
    mat2_np = MatrixWithNumPy(m2_list)

    print("Addition (Matrix 1 + Matrix 2):")
    mat1_np.add(mat2_np).display()

    print("\nSubtraction (Matrix 1 - Matrix 2):")
    mat1_np.subtract(mat2_np).display()

    print("\nMultiplication (Matrix 1 * Matrix 2):")
    mat1_np.multiply(mat2_np).display()

    print("\nTranspose of Matrix 1:")
    mat1_np.transpose().display()
	
