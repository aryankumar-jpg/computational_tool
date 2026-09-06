import sqlite3
DB_NAME = "employees.db"

def seed_sample_data():
    """Populates sample employee data for demonstration if table is empty."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""

            CREATE TABLE IF NOT EXISTS employees (

                emp_id TEXT PRIMARY KEY,

                name TEXT NOT NULL,

                designation TEXT NOT NULL,

                department TEXT NOT NULL,

                salary REAL NOT NULL
            )
        """)
        cursor.execute("SELECT COUNT(*) FROM employees")
        if cursor.fetchone()[0] == 0:
            sample_data = [

                ("E101", "Alice Smith", "Software Engineer", "Engineering", 85000.0),

                ("E102", "Bob Jones", "QA Lead", "Engineering", 75000.0),

                ("E103", "Charlie Brown", "DevOps Engineer", "Engineering", 90000.0),

                ("E104", "Diana Prince", "HR Manager", "HR", 70000.0),

                ("E105", "Evan Wright", "Recruiter", "HR", 55000.0),

                ("E106", "Fiona Gallagher", "Financial Analyst", "Finance", 80000.0),

                ("E107", "George Clark", "Accountant", "Finance", 65000.0)
            ]
            cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", sample_data)
            conn.commit()
def generate_summary_report():
    """Generates an aggregate salary overview grouped by department."""
    query = """
        SELECT 
            department,
            COUNT(emp_id) AS total_employees,
            SUM(salary) AS total_payroll,
            AVG(salary) AS avg_salary,
            MIN(salary) AS min_salary,
            MAX(salary) AS max_salary
        FROM employees
        GROUP BY department
        ORDER BY total_payroll DESC
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
 
        if not rows:
            print("\n[INFO] No employee data found to generate report.")
            return
            
        print("\n" + "=" * 80)
        print(" DEPARTMENT-WISE SALARY SUMMARY REPORT")
        print("=" * 80)
        print(f"{'Department':<15} | {'Headcount':<10} | {'Total Payroll':<15} | {'Avg Salary':<12} | {'Min / Max Range':<18}")
        print("-" * 80)
        for dept, count, total, avg_sal, min_sal, max_sal in rows:
            range_str = f"${min_sal:,.0f} - ${max_sal:,.0f}"
            print(f"{dept:<15} | {count:<10} | ${total:<14,.2f} | ${avg_sal:<11,.2f} | {range_str:<18}")
        print("=" * 80)
        
def generate_department_detail_report(department_name):
    """Executes a parameterized query to fetch individual employee salaries in a specific department."""
    query = """
        SELECT emp_id, name, designation, salary 
        FROM employees 
        WHERE LOWER(department) = LOWER(?)
        ORDER BY salary DESC
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (department_name,))
        rows = cursor.fetchall()
        if not rows:
            print(f"\n[INFO] No records found for department: '{department_name}'.")
            return
 
        print(f"\n--- Detailed Salary Breakdown: {department_name.upper()} ---")
        print(f"{'Emp ID':<10} | {'Name':<20} | {'Designation':<20} | {'Salary':<12}")
        print("-" * 68)
        total_dept_sal = 0
        for emp_id, name, desig, sal in rows:
            print(f"{emp_id:<10} | {name:<20} | {desig:<20} | ${sal:<11,.2f}")
            total_dept_sal += sal

        print("-" * 68)
        print(f"{'Total Department Expenditure:':<54} ${total_dept_sal:,.2f}")
def main_report_system():
    seed_sample_data()
    while True:
        print("\n--- Salary Report Generator ---")
        print("1. View Department Summary Report (All Departments)")
        print("2. View Detailed Report for a Specific Department")
        print("3. Exit")
 
        choice = input("Select an option (1-3): ").strip()
 
        if choice == "1":
            generate_summary_report()
        elif choice == "2":
            dept = input("Enter Department Name (e.g., Engineering, HR, Finance): ").strip()
            generate_department_detail_report(dept)
        elif choice == "3":
            print("Exiting Report Generator.")
            break
        else:
            print("[ERROR] Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main_report_system()

