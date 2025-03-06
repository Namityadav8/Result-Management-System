import random
import json

subjects = ["Electronics", "Programming", "Database", "Data Science", "Mathematics", "DSA"]

def generate_students(num_students=10000):
    students = []
    for i in range(1, num_students + 1):
        student = {
            "StudentID": f"S{i}",
            "Name": f"Student_{i}",
            "Marks": {subject: random.randint(0, 100) for subject in subjects}
        }
        students.append(student)
    return students

if __name__ == "__main__":
    students = generate_students()
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Student data generated successfully.")