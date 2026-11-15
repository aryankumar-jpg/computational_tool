import xml.etree.ElementTree as ET

tree = ET.parse('university_records.xml')
root = tree.getroot()

print("1. View Campus Details")
print("2. View Departments")
print("3. View Student Records")
choice = input("Enter your choice (1-3): ")

if choice == '1':
    campus = root.find('campus')
    print("\n--- Campus Information ---")
    print("Location:", campus.find('location').text)
    print("Established:", campus.find('established').text)
    print("Website:", campus.find('website').text)

elif choice == '2':
    print("\n--- Department Details ---")
    for dept in root.findall('.//department'):
        print("Department ID:", dept.get('id'))
        print("Name:", dept.find('name').text)
        print("HOD:", dept.find('hod').text)
        print("Building:", dept.find('building').text)
        print("-" * 30)

elif choice == '3':
    print("\n--- Student Records ---")
    for student in root.findall('.//student'):
        s_id = student.get('id')
        first = student.find('.//first_name').text
        last = student.find('.//last_name').text
        cgpa = student.find('academic_details/cgpa').text
        email = student.find('.//email').text
        print(f"ID: {s_id} | Name: {first} {last} | CGPA: {cgpa} | Email: {email}")

else:
    print("Invalid choice entered.")

