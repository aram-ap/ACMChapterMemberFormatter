# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv

def get_student_info():
    students = []
    input_format = input("Are the names entered separately, combined, or combined with email? (separately/combined/combined_with_email): ").strip().lower()

    while True:
        if input_format == 'separately':
            lastname = input("Enter last name (or 'done' to finish): ")
            if lastname.lower() == 'done':
                break
            lastname = lastname.split()[0]  # Use only the first word
            firstname = input("Enter first name: ")
            firstname = firstname.split()[0]  # Use only the first word
            email = input("Enter email: ")
        elif input_format == 'combined':
            name = input("Enter name in 'Lastname, Firstname' format (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            lastname, firstname = map(str.strip, name.split(','))
            lastname = lastname.split()[0]  # Use only the first word
            firstname = firstname.split()[0]  # Use only the first word
            email = input("Enter email: ")
        elif input_format == 'combined_with_email':
            entry = input("Enter entry in 'Lastname, Firstname\\tEmail' format (or 'done' to finish): ")
            if entry.lower() == 'done':
                break
            name, email = entry.split('\t')
            lastname, firstname = map(str.strip, name.split(','))
            lastname = lastname.split()[0]  # Use only the first word
            firstname = firstname.split()[0]  # Use only the first word
        else:
            print("Invalid input format. Please enter 'separately', 'combined', or 'combined_with_email'.")
            continue

        students.append((lastname, firstname, email))

    return students

def read_existing_students(filename='students.csv'):
    existing_students = {}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL)
            for row in reader:
                lastname, firstname, email = row
                existing_students[(lastname, firstname)] = email
    except FileNotFoundError:
        pass
    return existing_students

def write_to_csv(students, filename='students.csv'):
    existing_students = read_existing_students(filename)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for student in students:
            lastname, firstname, email = student
            if (lastname, firstname) in existing_students:
                if existing_students[(lastname, firstname)] != email:
                    existing_students[(lastname, firstname)] = email
            else:
                existing_students[(lastname, firstname)] = email

        for (lastname, firstname), email in existing_students.items():
            writer.writerow([lastname, firstname, email])

if __name__ == '__main__':
    students = get_student_info()
    write_to_csv(students)
    print("Student information has been written to students.csv")