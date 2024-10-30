from employee import Employee
from student import Student 
employees = []
students = []

def display_menu():
    print("""
    Add Employee : 1
    Add Student : 2
    Quit program : 0
        """)
    return input("Your choice (0/1/2): ")

def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print(f"Error: {prompt.strip()} cannot be empty!")
    
def get_person_details():
    prompts = ["Enter lastname: ", "Enter firstname: ", "Enter address: "]
    lastname, firstname, address = [get_valid_input(prompt) for prompt in prompts]
    return lastname, firstname, address

def add_employee():
        lastname, firstname, address = get_person_details()
        job_title = get_valid_input("Enter the employee's job title: ")
        employee = Employee(lastname, firstname, address, job_title)
        employees.append(employee)

def add_student():
        lastname, firstname, address = get_person_details()
        student = Student(lastname, firstname, address)
        while True:
            add_course = input("Would you like to add a course? (y/n): ").lower()
            if add_course == "y":
                course = get_valid_input("Course name: ")
                student.add_course(course)
            elif add_course == "n":
                break
            else:
                print("Invalid input. Please enter y or n")
        students.append(student)

def main():
    while True:
            choice = display_menu()

            if choice == "0":
                break
            elif choice == "1":
                add_employee()
            elif choice == "2":
                add_student()
            else:
                print("Invalid choice, please try again.")
    print("\nRegistered employee.s: ")
    for employee in employees:
        print(employee)
    print("\nRegistered student.s: ")   
    for student in students:
        print(student)

main()