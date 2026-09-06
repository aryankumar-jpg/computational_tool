import numpy as np

class matrixanalyzer:
	def __init__(self, matrix_data):
		self.matrix = np.array(matrix_data, dtype=float)
		
	def determinant(self):
		return np.linalg.det(self.matrix)
		
	def rank(self):
		return np.linalg.matrix_rank(self.matrix)
		
	def inverse(self):
		det  =self.determinant()
		if np.isclose(det, 0):
			return "matrix is singular; inverse does not exist."
		return np.linalg.inv(self.matrix)
		
	def summary(self):
		print("matrix:\n", self.matrix)
		print(f"\ndeterminant: {self.determinant():.4f}")
		print(f"rank: {self.rank()}")
		print("\ninverse matrix:\n", self.inverse())
		
if __name__ == "__main__":
	data = [
		[6, 1, 1],
		[4, -2, 5],
		[2, 8, 7]
	]
		
	analyzer= matrixanalyzer(data)
	analyzer.summary()
		
		
	
