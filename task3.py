class studentmanager:
	def __init__(self):
		
		self.students = []
		
	def insert(self,roll,name,age,grade):
	
		for student in self.students:
			if student["roll"] == roll:
				print(f"Error: student with roll number {roll} already exists.")
				return
				
		student_rec = {
			"roll": roll,
			"name": name,
			"age": age,
			"grade": grade
		}
		self.students.append(student_rec)
		print(f"Success: student '{name}' added successfully.")
		
	def search_student(self,roll):
	
		for student in self.students:
			if student["roll"] == roll:
				print("\nstudent found")
				print(f"roll number : {student['roll']}")
				print(f"name        : {student['name']}")
				print(f"age         : {student['age']}")
				print(f"grade       : {student['grade']}")
				return student
		print(f"Notice: student with roll number {roll} not found.")
		return none
		
	def delete_student(self,roll):
	
		for student in self.students:
			if student["roll"] == roll:
				self.students.remove(student)
				print(f"Success: student '{student['name']}' deleted successfully.")
				return
		print(f"Notice: student with roll number {roll} not found for deletion.")
		
	def display_all(self):
		
		if not self.students:
			print("no student records.")
			return
			
		
		print("\n all student records--")
		for student in self.students:
			print(f"Roll: {student['roll']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
		print("-" * 30)
		
		
		
if __name__ == "__main__":
	manager = studentmanager()
	
	manager.insert(101, "bhagat singh", 23, "A+")
	manager.insert(102, "shivaram rajuru", 22, "B")
	manager.insert(103, "sukhdev thapar", 23, "A")
	manager.insert(104, "subhash chandra bose", 48, "A")
	
	manager.display_all()
	
	manager.search_student(102)
	
	manager.delete_student(104)
	
	manager.display_all()
	
		
	
	
	
	
	
	
	
		
			
				
		
		
				
						
