from student import Student
from employee import Employee

employees = []
students = []

def display_menu():
    print("""
    Add Employee : 1
    Add Student : 2
    Quit program : 0
        """)
    return input("Your choice (0/1/2): ")

get_valid_input = lambda prompt: (input(prompt) or get_valid_input(f"Error: {prompt} cannot be empty."))
    
def get_person_details():
    prompts = ["Enter lastname: ", "Enter firstname: ", "Enter address: "]
    lastname, firstname, address = map(get_valid_input, prompts)
    return lastname, firstname, address

def add_employee():
    try: 
        lastname, firstname, address = get_person_details()
        job_title = get_valid_input("Enter the employee's job title: ")
        employee = Employee(lastname, firstname, address, job_title)
        employees.append(employee)
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
        add_employee() 

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