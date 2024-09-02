

from abc import ABC, abstractmethod

class StudentManagementSystem(ABC):
    @abstractmethod
    def add_student(self):
        pass

    @abstractmethod
    def view_students(self):
        pass

    @abstractmethod
    def update_student(self):
        pass

    @abstractmethod
    def delete_student(self):
        pass

    @abstractmethod
    def search_student(self):
        pass

    @abstractmethod
    def sort_students(self):
        pass

    @abstractmethod
    def filter_students(self):
        pass

class School(StudentManagementSystem):
    def __init__(self):
        self.students = []

    def title(self):
        print("Student Management System")

    def add_student(self):
        id = input("\nEnter Student ID: ")
        if any(student['id'] == id for student in self.students):
            print("Student ID already exists.")
            return
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        grade = input("Enter Student Grade: ")
        email = input("Enter Student Email: ")
        self.students.append({
            'id': id,
            'name': name,
            'age': age,
            'grade': grade,
            'email': email
        })
        print("Student Added Successfully")

    def view_students(self):
        print("\nList of Students:")
        for sno, student in enumerate(self.students, 1):
            print(f"{sno}. ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Email: {student['email']}")

    def update_student(self):
        id = input("\nEnter the ID of the student you want to update: ")
        student = next((student for student in self.students if student['id'] == id), None)
        if student:
            name = input("Enter the new name: ")
            age = input("Enter the new age: ")
            grade = input("Enter the new grade: ")
            email = input("Enter the new email: ")
            student.update({
                'name': name,
                'age': age,
                'grade': grade,
                'email': email
            })
            print("Student Updated Successfully")
        else:
            print("Student Not Found")

    def delete_student(self):
        id = input("\nEnter the ID of the student you want to remove: ")
        self.students = [student for student in self.students if student['id'] != id]
        print("Student Removed Successfully")

    def search_student(self):
        name = input("\nEnter the name of the student you want to search: ")
        found_students = [student for student in self.students if name.lower() in student['name'].lower()]
        if found_students:
            for student in found_students:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Email: {student['email']}")
        else:
            print("No students found with that name")

    def sort_students(self):
        print("\nSort Students by:")
        print("1. Name")
        print("2. Age")
        print("3. Grade")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.students.sort(key=lambda x: x['name'])
        elif choice == '2':
            self.students.sort(key=lambda x: int(x['age']))
        elif choice == '3':
            self.students.sort(key=lambda x: x['grade'])
        else:
            print("Invalid choice")
        self.view_students()

    def filter_students(self):
        print("\nFilter Students by:")
        print("1. Grade")
        print("2. Age")
        choice = input("Enter your choice: ")
        if choice == '1':
            grade = input("Enter the grade: ")
            filtered_students = [student for student in self.students if student['grade'] == grade]
            for student in filtered_students:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Email: {student['email']}")
        elif choice == '2':
            age = input("Enter the age: ")
            filtered_students = [student for student in self.students if student['age'] == age]
            for student in filtered_students:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Email: {student['email']}")
        else:
            print("Invalid choice")

obj = School()
obj.title()
while True:
    print("\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Sort Students")
    print("7. Filter Students")
    print("8. Exit")
    data = int(input("\nPlease Enter Your Operation: "))
    if data == 1:
        obj.add_student()
    elif data == 2:
        obj.view_students()
    elif data == 3:
        obj.update_student()
    elif data == 4:
        obj.delete_student()
    elif data == 5:
        obj.search_student()
    elif data == 6:
        obj.sort_students()
    elif data == 7:
        obj.filter_students()
    elif data == 8:
        print("Exiting...")
        break
    else:
        print("Invalid Option. Please try again.")

