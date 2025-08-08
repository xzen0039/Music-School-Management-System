# Music School Management System (MSMS) – In-Memory Prototype

Version: 1.0  
Author: Xianghao Zeng  
Stage: PST1 – Foundation / In-Memory Prototype

---

## Overview

The Music School Management System (MSMS) is a console-based prototype designed to simulate the core operations of a music school.  
This PST1 version operates entirely **in-memory**, meaning all data is lost when the program exits. It serves as a foundation for future stages that will introduce persistent storage, richer user interfaces, and expanded functionality.

The system models **Students**, **Teachers**, and their relationships, and provides an interactive menu for front desk and administrative tasks.

---

## Features

### Data Models
- `Student`
  - Stores student ID, name, and a list of enrolled instruments.
- `Teacher`
  - Stores teacher ID, name, and teaching speciality.

### Core Functionalities
1. **Add Teachers** – Create new teachers with a name and speciality.
2. **Add Students** – Create new students with unique IDs.
3. **Enroll Students** – Assign instruments to students.
4. **Search** – Find students or teachers by name/speciality (case-insensitive).
5. **List All Records** – Display all students or teachers.
6. **Generate Sample Data** – Populate the system with example teachers and students for testing.

### Interactive Menu
- Option `1`: Register a new student and enroll them in an instrument.
- Option `2`: Enroll an existing student in an additional instrument.
- Option `3`: Search for students/teachers by name or speciality.
- Option `4`: List all students.
- Option `5`: List all teachers.
- Option `6`: Add a new teacher.
- Option `7`: Generate sample data.
- Option `q`: Quit the program.

---

## How to Run

### Requirements
- Python 3.7+ installed on your system.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Music-School-Management-System.git
   cd Music-School-Management-System
2. Run the program in the terminal:
   ```bash
   python MSMS.py
3. Follow the on-screen menu to interact with the system.

## How to Test
You can test functionality in two main ways:

1. Manual Testing via Menu
Launch the program and select various menu options.

Use Option 7 ("Generate Sample Data") to pre-load teachers and students, then test search, listing, and enrollment.

2. Programmatic Testing
   Import functions from MSMS.py into another Python script or interactive shell:
   ```python
   from MSMS import add_teacher, add_student, list_students, generate_sample_data

   generate_sample_data()
   list_students()

### Design Choices & Assumptions
1. In-Memory Data Storage
  This version uses Python lists (student_db, teacher_db) to store records.
  No external database is connected in PST1.

2. Auto-Increment IDs
  next_student_id and next_teacher_id track the next available IDs automatically.

3. Loose Coupling Between Roles
  Students are linked to instruments (by name), not directly to specific teachers.
  Future versions may link students to teacher IDs for more granular tracking.

4. Case-Insensitive Search
  All search queries are converted to lowercase for consistent matching.

5.No Input Validation Beyond Menu
  Minimal input checking is performed (e.g., numeric ID validation).
  Future versions may include stricter input validation and error handling.

6. Single-Threaded CLI Application
  Designed for simple, sequential use at the front desk.
