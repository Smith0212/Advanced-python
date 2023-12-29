import csv

def read_student_grades(filename):
    student_grades = {}
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        # print (reader)
        for row in reader:
            # print (row)
            name = row['Name']
            math = float(row['Maths'])
            science = float(row['Science'])
            english = float(row['English'])
            student_grades[name] = [math, science, english]
    return student_grades

def calculate_average(student_grades):
    student_average = {}
    for name, grades in student_grades.items():
        average = sum(grades) / len(grades)
        student_average[name] = average
    return student_average

def write_student_average_to_csv(filename, student_average):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Average'])
        for name, average in student_average.items():
            writer.writerow([name, average])

if __name__ == "__main__":
    student_grades_data = read_student_grades("Q1\student_grades.csv")
    student_average_data = calculate_average(student_grades_data)
    write_student_average_to_csv("student_average_grades.csv", student_average_data)
    print("File written successfully")
