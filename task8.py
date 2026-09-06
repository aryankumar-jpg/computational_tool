import numpy as np

midsemmarks=np.array([
	[65,70,68,72],
	[78,75,80,77],
	[55,60,68,62],
	[82,85,80,88],
	[70,68,72,74]
])
endsemmarks=np.array([
	[72,78,75,80],
	[84,82,86,83],
	[65,68,66,70],
	[88,90,85,92],
	[78,75,80,82]
])

total_marks =np.sum(endsemmarks, axis=1)
avg_marks =np.sum(endsemmarks, axis=1)
midsem_total=np.sum(midsemmarks, axis=1)
endsem_total=np.sum(endsemmarks, axis=1)
percentage_improvement= ((endsem_total-midsem_total) / midsem_total) * 100

students = ["s1", "s2", "s3", "s4", "s5"]
print(f"{'student':<10}{'total marks':<15}{'average marks':<15}{'improvement (%)':<15}")
print("-" * 55)
for i, student in enumerate(students):
	print(f"{'student':<10}{total_marks[i]:<15}{avg_marks[i]:<15.2f}{percentage_improvement[i]:<15.2f}")	
