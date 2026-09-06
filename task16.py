import sqlite3

DATABASE_NAME = "students.db"

def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                cgpa REAL NOT NULL CHECK(cgpa >= 0.0 AND cgpa <= 10.0)
            )
        """)
        conn.commit()

def add_student(roll_no, name, department, cgpa):
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (roll_no, name, department, cgpa) VALUES (?, ?, ?, ?)",
                (roll_no, name, department, cgpa)
            )
            conn.commit()
            print(f"[SUCCESS] Student '{name}' (Roll No: {roll_no}) added successfully.")
    except sqlite3.IntegrityError:
        print(f"[ERROR] A student with Roll No '{roll_no}' already exists.")

def get_student_by_roll(roll_no):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT roll_no, name, department, cgpa FROM students WHERE roll_no = ?", (roll_no,))
        row = cursor.fetchone()
        
        if row:
            print("\n--- Student Details ---")
            print(f"Roll No : {row[0]}")
            print(f"Name : {row[1]}")
            print(f"Department : {row[2]}")
            print(f"CGPA : {row[3]:.2f}")
            print("-----------------------")
        else:
            print(f"[NOT FOUND] No record found for Roll No '{roll_no}'.")

def display_all_students():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT roll_no, name, department, cgpa FROM students ORDER BY roll_no")
        rows = cursor.fetchall()
        
        if not rows:
            print("\n[INFO] No student records available.")
            return

        print("\n" + "=" * 60)
        print(f"{'Roll No':<12} | {'Name':<20} | {'Department':<15} | {'CGPA':<5}")
        print("=" * 60)
        for roll_no, name, dept, cgpa in rows:
            print(f"{roll_no:<12} | {name:<20} | {dept:<15} | {cgpa:<5.2f}")
        print("=" * 60)

def main_student_system():
    init_db()
    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. Search Student by Roll No")
        print("3. Display All Students")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            roll = input("Enter Roll Number: ").strip()
            name = input("Enter Name: ").strip()
            dept = input("Enter Department: ").strip()
            try:
                cgpa = float(input("Enter CGPA (0.0 - 10.0): ").strip())
                if 0.0 <= cgpa <= 10.0:
                    add_student(roll, name, dept, cgpa)
                else:
                    print("[ERROR] CGPA must be between 0.0 and 10.0.")
            except ValueError:
                print("[ERROR] Invalid CGPA format.")
        elif choice == "2":
            roll = input("Enter Roll Number to search: ").strip()
            get_student_by_roll(roll)
        elif choice == "3":
            display_all_students()
        elif choice == "4":
            print("Exiting Student Management System.")
            break
        else:
            print("[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    main_student_system()


