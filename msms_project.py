# MSMS.py - The In-Memory Prototype (PST1 Complete)
# Version: 1.0
# Author: Xianghao Zeng
# Description: Music School Management System - Foundation Stage

# --- Data Models ---
class Student:
    """Represents a student in the music school"""
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.enrolled_in = []  # List of instruments student is enrolled in

    def __str__(self):
        return f"Student(ID={self.id}, Name={self.name}, Instruments={self.enrolled_in})"

class Teacher:
    """Represents a music teacher"""
    def __init__(self, teacher_id, name, speciality):
        self.id = teacher_id
        self.name = name
        self.speciality = speciality
    
    def __str__(self):
        return f"Teacher(ID={self.id}, Name={self.name}, Speciality={self.speciality})"

# --- In-Memory Databases ---
student_db = []
teacher_db = []
next_student_id = 1
next_teacher_id = 1

# --- Core Helper Functions ---
def add_teacher(name, speciality):
    """Creates a Teacher object and adds it to the database"""
    global next_teacher_id
    new_teacher = Teacher(next_teacher_id, name, speciality)
    teacher_db.append(new_teacher)
    next_teacher_id += 1
    print(f"Core: Teacher '{name}' ({speciality}) added successfully. ID: {new_teacher.id}")
    return new_teacher.id

def add_student(name):
    """Creates a Student object and adds it to the database"""
    global next_student_id
    new_student = Student(next_student_id, name)
    student_db.append(new_student)
    next_student_id += 1
    print(f"Core: Student '{name}' added successfully. ID: {new_student.id}")
    return new_student.id

def list_students():
    """Prints all students in the database"""
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system")
        return
    
    for student in student_db:
        instruments = ', '.join(student.enrolled_in) if student.enrolled_in else "None"
        print(f"  ID: {student.id}, Name: {student.name}, Instruments: {instruments}")

def list_teachers():
    """Prints all teachers in the database"""
    print("\n--- Teacher List ---")
    if not teacher_db:
        print("No teachers in the system")
        return
    
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def find_students(term):
    """Finds students by name (case-insensitive)"""
    term = term.lower()
    results = []
    
    for student in student_db:
        if term in student.name.lower():
            results.append(student)
    
    return results

def find_teachers(term):
    """Finds teachers by name or speciality (case-insensitive)"""
    term = term.lower()
    results = []
    
    for teacher in teacher_db:
        if (term in teacher.name.lower()) or (term in teacher.speciality.lower()):
            results.append(teacher)
    
    return results

# --- Front Desk Functions ---
def find_student_by_id(student_id):
    """Finds a student by their ID"""
    for student in student_db:
        if student.id == student_id:
            return student
    return None

def find_teacher_by_id(teacher_id):
    """Finds a teacher by their ID"""
    for teacher in teacher_db:
        if teacher.id == teacher_id:
            return teacher
    return None

def front_desk_register(name, instrument):
    """Registers a new student and enrolls them in an instrument"""
    global next_student_id
    student_id = add_student(name)
    front_desk_enrol(student_id, instrument)
    return student_id

def front_desk_enrol(student_id, instrument):
    """Enrolls an existing student in an instrument"""
    student = find_student_by_id(student_id)
    
    if student:
        if instrument not in student.enrolled_in:
            student.enrolled_in.append(instrument)
            print(f"Front Desk: Enrolled student {student_id} ({student.name}) in '{instrument}'")
        else:
            print(f"Front Desk: Student {student_id} already enrolled in '{instrument}'")
    else:
        print(f"Error: Student ID {student_id} not found")

def front_desk_lookup(term):
    """Searches for students and teachers matching a term"""
    print(f"\n--- Search Results for '{term}' ---")
    
    # Find matching students
    student_results = find_students(term)
    if student_results:
        print(f"\nStudents ({len(student_results)} found):")
        for student in student_results:
            instruments = ', '.join(student.enrolled_in) if student.enrolled_in else "None"
            print(f"  ID: {student.id}, Name: {student.name}, Instruments: {instruments}")
    else:
        print("\nNo matching students found")

# Find matching teachers
    teacher_results = find_teachers(term)
    if teacher_results:
        print(f"\nTeachers ({len(teacher_results)} found):")
        for teacher in teacher_results:
            print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")
    else:
        print("\nNo matching teachers found")

# --- Admin Functions ---
def generate_sample_data():
    """Creates sample data for testing"""
    print("\nGenerating sample data...")
    
    # Add sample teachers
    add_teacher("Dr. Keys", "Piano")
    add_teacher("Ms. Fret", "Guitar")
    add_teacher("Mr. Bow", "Violin")
    
    # Add sample students and enrollments
    s1 = front_desk_register("Alice Johnson", "Piano")
    front_desk_enrol(s1, "Violin")
    
    front_desk_register("Bob Smith", "Guitar")
    front_desk_register("Charlie Brown", "Drums")
    
    print("Sample data generated successfully")

# --- Main Application ---
def main_menu():
    """Displays the main menu"""
    print("\n===== Music School Front Desk =====")
    print("1. Register New Student")
    print("2. Enroll Existing Student")
    print("3. Search Student or Teacher")
    print("4. List All Students")
    print("5. List All Teachers")
    print("6. Add New Teacher")
    print("7. Generate Sample Data")
    print("q. Quit")

def main():
    """Runs the main interactive menu"""
    # Initial sample data
    generate_sample_data()
    
    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            name = input("Enter student name: ").strip()
            instrument = input("Enter instrument to enroll in: ").strip()
            front_desk_register(name, instrument)
        
        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: ").strip())
                instrument = input("Enter instrument to enroll in: ").strip()
                front_desk_enrol(student_id, instrument)
            except ValueError:
                print("Error: Invalid ID format. Please enter a number")
        
        elif choice == '3':
            term = input("Enter search term (name or speciality): ").strip()
            if term:
                front_desk_lookup(term)
            else:
                print("Error: Please enter a search term")
        
        elif choice == '4':
            list_students()
        
        elif choice == '5':
            list_teachers()
        
        elif choice == '6':
            name = input("Enter teacher name: ").strip()
            speciality = input("Enter teacher speciality: ").strip()
            add_teacher(name, speciality)
        
        elif choice == '7':
            generate_sample_data()
        
        elif choice.lower() == 'q':
            print("\nExiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again")
        
# --- Program Start ---
if __name__ == "__main__":
    print("=== Music School Management System ===")
    print("Stage: PST1 - In-Memory Prototype\n")
    main()
    
