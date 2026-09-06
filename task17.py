import sqlite3
DB_NAME = "employees.db"

def init_employee_db():
    """Initializes the database and creates the employees table."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""

            CREATE TABLE IF NOT EXISTS employees (

                emp_id TEXT PRIMARY KEY,

                name TEXT NOT NULL,

                designation TEXT NOT NULL,

                department TEXT NOT NULL,

                salary REAL NOT NULL CHECK(salary >= 0)

            )
        """)
        conn.commit()

def create_employee(emp_id, name, designation, department, salary):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (emp_id, name, designation, department, salary) VALUES (?, ?, ?, ?, ?)",
                (emp_id, name, designation, department, salary)
            )
            conn.commit()
            print(f"[SUCCESS] Employee {name} (ID: {emp_id}) added.")
    except sqlite3.IntegrityError:
        print(f"[ERROR] Employee ID '{emp_id}' already exists.")

def read_all_employees():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id, name, designation, department, salary FROM employees")
        records = cursor.fetchall()
        if not records:
            print("\n[INFO] No employee records found.")
            return

        print("\n" + "=" * 75)
        print(f"{'Emp ID':<10} | {'Name':<18} | {'Designation':<15} | {'Dept':<12} | {'Salary':<10}")
        print("=" * 75)
        for emp_id, name, desig, dept, sal in records:
            print(f"{emp_id:<10} | {name:<18} | {desig:<15} | {dept:<12} | ${sal:<10,.2f}")
        print("=" * 75)

def read_employee_by_id(emp_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id, name, designation, department, salary FROM employees WHERE emp_id = ?", (emp_id,))
        emp = cursor.fetchone()
        
        if emp:
            print(f"\nID: {emp[0]} | Name: {emp[1]} | Designation: {emp[2]} | Department: {emp[3]} | Salary: ${emp[4]:,.2f}")
        else:
            print(f"[NOT FOUND] No employee found with ID '{emp_id}'.")


def update_employee(emp_id, designation=None, department=None, salary=None):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id, name, designation, department, salary FROM employees WHERE emp_id = ?", (emp_id,))
        existing = cursor.fetchone()
        if not existing:
            print(f"[ERROR] Employee with ID '{emp_id}' not found.")
            return

        new_desig = designation if designation else existing[2]
        new_dept = department if department else existing[3]
        new_sal = salary if salary is not None else existing[4]

        cursor.execute("""
            UPDATE employees
            SET designation = ?, department = ?, salary = ?
            WHERE emp_id = ?
        """, (new_desig, new_dept, new_sal, emp_id))
        conn.commit()
        print(f"[SUCCESS] Employee ID '{emp_id}' successfully updated.")

def delete_employee(emp_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"[SUCCESS] Employee ID '{emp_id}' deleted.")
        else:
            print(f"[ERROR] Employee ID '{emp_id}' not found.")
def main_crud_system():
    init_employee_db()
    while True:
        print("\n--- Employee CRUD Manager ---")
        print("1. Create (Add Employee)")
        print("2. Read (View All Employees)")
        print("3. Read (Search Employee by ID)")
        print("4. Update (Edit Employee)")
        print("5. Delete (Remove Employee)")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            emp_id = input("Employee ID: ").strip()
            name = input("Name: ").strip()
            desig = input("Designation: ").strip()
            dept = input("Department: ").strip()
            try:
                salary = float(input("Salary: ").strip())
                create_employee(emp_id, name, desig, dept, salary)
            except ValueError:
                print("[ERROR] Invalid salary input.")
        elif choice == "2":
            read_all_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ").strip()
            read_employee_by_id(emp_id)
        elif choice == "4":
            emp_id = input("Enter Employee ID to update: ").strip()
            desig = input("New Designation (leave blank to keep current): ").strip()
            dept = input("New Department (leave blank to keep current): ").strip()
            sal_input = input("New Salary (leave blank to keep current): ").strip()
            sal = float(sal_input) if sal_input else None
            update_employee(emp_id, desig or None, dept or None, sal)

        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ").strip()
            delete_employee(emp_id)

        elif choice == "6":
            print("Exiting Employee Manager.")
 
            break
        else:
            print("[ERROR] Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main_crud_system()
