def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def process_students(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        results = []
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 2:
                continue

            name = parts[0].strip()
            marks = [float(mark.strip()) for mark in parts[1:]]

            total = sum(marks)
            average = total / len(marks) if marks else 0
            grade = calculate_grade(average)

            results.append(
                f"Name: {name}, Marks: {marks}, Total: {total:.2f}, Average: {average:.2f}, Grade: {grade}\n"
            )

        with open(output_file, "w") as outfile:
            outfile.writelines(results)

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")

if __name__ == "__main__":
    process_students("students.txt", "output.txt")
