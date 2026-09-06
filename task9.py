import numpy as np

datasets = {
	"marks": [78,85,92,67,88,73,95,81,76,89],
	"temperatures": [28.5,30.2,29.8,31.4,27.9,32.1,30.5],
	"sales": [12500,13800,14200,11900,15100,14700,16000]
}

for name, data in datasets.items():
	print(f"\n====== {name} ======")
	
	n= len(data)
	sorted_data =sorted(data)
	
	mean_no_np = sum(data) / n
	
	if n%2 == 1:
		median_no_np = sorted_data[n // 2]
	else:
		median_no_np = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
		
	min_no_np = sorted_data[0]
	max_no_np = sorted_data[-1]
	
	variance_no_np = sum((x-mean_no_np) ** 2 for x in data) / n
	std_no_np = variance_no_np ** 0.5
	
	print("without numpy:")
	print(f"mean:   {mean_no_np:.2f}")
	print(f"median: {median_no_np}")
	print(f"min:    {min_no_np}")
	print(f"max:    {max_no_np}")
	print(f"std:    {std_no_np:.2f}")
	
	arr=np.array(data)
	
	mean_np = np.mean(arr)
	median_np = np.median(arr)
	min_np = np.min(arr)
	max_np = np.max(arr)
	std_np = np.std(arr)
	
	print("\nwith numpy:")
	print(f"mean:   {mean_np:.2f}")
	print(f"median: {median_np}")
	print(f"min:    {min_np}")
	print(f"max:    {max_np}")
	print(f"std:    {std_np:.2f}")
		
		 
