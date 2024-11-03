from datetime import date

employees = []  # List to hold employees data
today = date.today()
menu_options = [
                "Add Employee",
                "Display All Employees Data",
                "Display One Employee Data by id",
                "Update Employee",
                "Remove Employee",
                "Search Employee by id",
                "Search Employee by name",
                "Sorting Employee Data by joining date",
                "Display Employee Data With low and high salary",
                "Get The total salary for each department",
                "Get the first and last employee",
                "Exit From The Program"
                ]
# ---------------------------------   ***  ------------------------------------
def generate_new_id():
    if not employees:
        return 1
    else:
        return (employees[-1]['emp_id']) + 1
# ---------------------------------------------------------------------------
def add_employee(*args):
    id =  generate_new_id()
    employee = {
        'emp_id': id,
        'name': args[0],
        'joining_date': today.strftime("%Y-%m-%d"),
        'salary': args[1],
        'department': args[2]
    }
    employees.append(employee)
    print(f"Employee {args[0]} added successfully by this id {id}!")
# ---------------------------------------------------------------------
def isFound(id):
    for emp in employees:
        if emp['emp_id'] == id:
            return  True
    return False
# ---------------------------------------------------------------------
def updte_employee(*args):
    for emp in employees:
        if emp['emp_id'] == args[0]:
            emp['name'] = args[1]
            emp['joining_date'] = today.strftime("%Y-%m-%d")
            emp['salary'] = args[2]
            emp['department'] = args[3]
            print(f"Employee {args[0]} updated successfully!")
            return
    print('No Employee by this id.')
# -------------------------------------------------------------------------
def delete_employee(emp_id):
    for emp in employees:
        if emp['emp_id'] == emp_id:
            employees.remove(emp)
            print(f"Employee {emp_id} removed successfully!")
            return
    print("Employee not found.")
# -------------------------------------------------------------------------
def searching_by_id(id):
    i = 0
    for emp in employees:
        if emp['emp_id'] == id:
            i = i + 1
            view_employee_data(i-1)
            return
    print('No Employee by this id.')
# -------------------------------------------------------------------------
def searching_by_name(name):
    i = 0
    for emp in employees:
        if emp['name'] == name:
            i = i + 1
            view_employee_data(i-1)
            return
    print('No Employee by this name.')
# ------------------------------------------------------------------------
def view_employee_data(index): # show  data for one employee
    emp = employees[index]
    print(f"ID: {emp['emp_id']}, Name: {emp['name']}, Joining Date: {emp['joining_date']}, Salary: {emp['salary']}, Department: {emp['department']}")
# ------------------------------------------------------------------------
def display_all_employees_data():
    if not employees: # check if list is not have elements
        print("No employees founds to display.")
    else:
        print("\n\t\tEmployee List:")
        for emp in employees:
            print(f"ID: {emp['emp_id']}, Name: {emp['name']}, Joining Date: {emp['joining_date']}, Salary: {emp['salary']}, Department: {emp['department']}")
            print("---------------------------------------------------------------------------------")
# -----------------------------------------------------------------------
def get_employee_with_low_salary():
    return min(employees, key=lambda x: x['salary'])  # here used the min FUN. to get minimum valu
#------------------------------------------------------------------------
def get_employee_with_high_salary():
    return max(employees, key=lambda x: x['salary'])
# ------------------------------------------------------------------------
def sorting_by_join_date():
    employees.sort(key=lambda x: x['joining_date'])
# -----------------------------------------------------------------------
def total_salaries_for_each_department():
    department_salaries = {}
    for emp in employees:  # loop on all Employees , to get departement for each one
        department = emp['department']
        salary = emp['salary']

        if department in department_salaries:  # if this department added to list , add it's salary to salary list
            department_salaries[department] += salary
        else:
            department_salaries[department] = salary

    print("\n\t\tTotal Salaries by Department:")
    for department, total_salary in department_salaries.items():
        print(f"Department: {department}, Total Salaries: {total_salary}")
# ------------------------------------------------------------------------
def Get_the_first_and_last_employees():
    sorting_by_join_date()
    first_employee = employees[0]
    last_employee = employees[-1]
    print("First Employee:", first_employee)
    print("Last Employee:", last_employee)
# ------------------------------------------------------------------------

def menu():
    while True:
        print('\n')
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        try:    # Handle errors
            choice = input("Please ,, Enter your choice here:  ")
            if choice == '1':
                name = input("Enter Employee Name: ")
                salary = float(input("Enter Salary: "))
                department = input("Enter Department: ")
                add_employee(name, salary, department)

            elif choice == '2':
                display_all_employees_data()

            elif choice == '3':
                searching_by_id(int(input("Enter The Employee id: ")))

            elif choice == '4':
                id = int(input("Enter The Employee id:  "))
                if isFound(id):
                    name = input("Enter Employee Name: ")
                    salary = float(input("Enter Salary: "))
                    department = input("Enter Department: ")
                    updte_employee(id, name, salary, department)

            elif choice == '5':
                delete_employee(int(input("Enter The Employee id: ")))

            elif choice == '6':
                searching_by_id(int(input("Enter The Employee id: ")))

            elif choice == '7':
                searching_by_name((input("Enter The Employee name: ")))

            elif choice == '8':
                sorting_by_join_date()
                view_employee_data()

            elif choice == '9':
                low_salary = get_employee_with_low_salary()
                high_salary = get_employee_with_high_salary()
                print('The Employee with low salary is: ' , low_salary)
                print('The Employee with high salary is: ' , high_salary)

            elif choice == '10':
                total_salaries_for_each_department()

            elif choice == '11':
                Get_the_first_and_last_employees()

            elif choice == '12':
                print("Finish the program. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError as e:
            print('There is an Error is happen : ' , str(e))
        except Exception as e:  # handle any Exception
            print('There is an Error is happen :  ', str(e))
# ---------------------------------   ***  ------------------------------------

# <<<<<<<<<<<<<<<<<<<<<<<<<<  Start The Program  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    print("\t\t<<< Employees Management System >>>")
    print("\t\t ===============================")
    menu() # calling the menue FUN. to execute the tasks.
# <<<<<<<<<<<<<<<<<<<<<<<<<<  End The Program  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>