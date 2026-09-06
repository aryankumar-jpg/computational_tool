std_1 = (101, "kurosawa")
std_2 = (102, "kubrick")
std_3 = (103, "scorcesse")
std_4 = (104, "fincher")
std_5 = (105, "satyajit ray")

std_directory = {
	std_1[0]: std_1,
	std_2[0]: std_2,
	std_3[0]: std_3,
	std_4[0]: std_4,
	std_5[0]: std_5
}

python_course = {101, 102, 103, 104}
java_course = {105, 103, 104}
webdev_course = {101, 103, 105}

def print_std_names(id_set):
	return [std_directory[sid][1] for sid in id_set]
	
print("course enrollment analysis--")
print(f"python course enrolled ids: {python_course}")
print(f"java course enrolled ids: {java_course}")
print(f"webdev course enrolled ids: {webdev_course}\n")

all_python_java = python_course.union(java_course)
print("1. UNION: student enrolled in python or java (or both):")
print(f"   IDs: {all_python_java}")
print(f"   Names: {print_std_names(all_python_java)}\n")

common_python_web = python_course.intersection(webdev_course)
print("2. INTERSECTION: student enrolled in both python and webdev:")
print(f"   IDs: {common_python_web}")
print(f"   Names: {print_std_names(common_python_web)}\n")

python_only = python_course.difference(java_course)
print("3. DIFFERENCE: student enrolled in python only (exclusive of java):")
print(f"   IDs: {python_only}")
print(f"   Names: {print_std_names(python_only)}\n")

complex_analysis = (python_course.intersection(webdev_course)).difference(java_course)
print("4. CHAINED: student enrolled in python and webdev, but excluded from java:")
print(f"   IDs: {complex_analysis}")
print(f"   Names: {print_std_names(complex_analysis)}\n")


