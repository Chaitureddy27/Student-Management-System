import json
import os

FILE_NAME = "students.json"

# Load data
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    data.append(student)
    save_data(data)
    print("✅ Student Added Successfully!\n")

# View students
def view_students():
    data = load_data()
    if not data:
        print("No students found.\n")
        return

    print("\n📋 Student List:")
    for s in data:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    print()

# Search student
def search_student():
    data = load_data()
    roll = input("Enter Roll Number to search: ")

    for s in data:
        if s["roll"] == roll:
            print(f"Found: {s}\n")
            return

    print("❌ Student not found.\n")

# Update student
def update_student():
    data = load_data()
    roll = input("Enter Roll Number to update: ")

    for s in data:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["age"] = input("Enter New Age: ")
            s["course"] = input("Enter New Course: ")
            save_data(data)
            print("✅ Updated Successfully!\n")
            return

    print("❌ Student not found.\n")

# Delete student
def delete_student():
    data = load_data()
    roll = input("Enter Roll Number to delete: ")

    new_data = [s for s in data if s["roll"] != roll]

    if len(new_data) == len(data):
        print("❌ Student not found.\n")
    else:
        save_data(new_data)
        print("✅ Deleted Successfully!\n")

# Main menu
def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()