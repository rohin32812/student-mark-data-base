import sqlite3

# Connect to database
conn = sqlite3.connect("student_marks.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")
conn.commit()


def add_student():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))

    cursor.execute(
        "INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)",
        (name, subject, marks)
    )
    conn.commit()
    print("Student record added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nStudent Records")
    print("-" * 40)
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}, Marks: {row[3]}")


def update_marks():
    student_id = int(input("Enter student ID: "))
    new_marks = int(input("Enter new marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )
    conn.commit()
    print("Marks updated successfully!")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student record deleted successfully!")


while True:
    print("\n===== Student Marks Database =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

conn.close()