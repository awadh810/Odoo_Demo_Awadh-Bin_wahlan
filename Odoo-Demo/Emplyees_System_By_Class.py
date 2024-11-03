from datetime import date
today = date.today()
emplyee_list = []
menu_options = [
                "Add Employee",
                "Update Employee",
                "Remove Employee",
                "Display All Employees Data",
                "Exit From The Program"
                ]
# --------------------------------------- ***------------------------------------------
class Employees:
    employee_counter_id = 1
    def __init__(self, emp_data):  # constructor Method
        self.name = emp_data.get("name")
        self.salary = emp_data.get("salary")
        self.joining_date = today.strftime("%Y-%m-%d")
        year, month, day = map(int, self.joining_date.split('-'))
        self.emp_id = int(f"{year}{month}{day}{Employees.employee_counter_id}")  # Mixed uniqu id

        Employees.employee_counter_id +=1
    # ----------------------------------------------------------------------------------------
    def save_Employee_data(self):  # instance for any obj from the class
        try:
            emplyee_list.append(self)
            print(f"Employee {self.emp_id} saved successfully.")
        except Exception as e:  # handle any Exception
            print('There is an Error is happen :  ', str(e))
    # ----------------------------------------------------------------------------------------
    @staticmethod   # get this method by class name
    def create_Employee(emp_data):
        try:
            new_emp = Employees(emp_data)
            new_emp.save_Employee_data()
        except Exception as e:  # handle any Exception
            print('There is an Error is happen :  ', str(e))
    # ----------------------------------------------------------------------------------------
    @staticmethod
    def update_Employee_data(emp_id , updated_data):
        try:
            if emplyee_list:
                for emp in emplyee_list:
                    if emp.emp_id == emp_id:
                        if updated_data.get("name"):    # the get method is more secure , don't retrieve an error if "name" not found
                            emp.name = updated_data["name"]
                        if updated_data.get("joining_date"):
                            emp.joining_date = updated_data["joining_date"]
                        if updated_data.get("salary"):
                            emp.salary = updated_data["salary"]
                        print(f"Employee {emp_id} updated successfully!")
                        return
        except Exception as e:  # handle any Exception
            print('There is an Error is happen :  ', str(e))

    # ----------------------------------------------------------------------------------------
    @staticmethod
    def delete_Employee(emp_id):
        i = 0
        try:
            if emplyee_list:  # to check if list not empty
                for emp in emplyee_list:
                    if emp.emp_id == emp_id:
                        emplyee_list.pop(i)
                        print('Employee is deleted Successfully.')
                        return
                    i += 1
            print('No Employees Found.')
        except Exception as e:  # handle any Exception
            print('There is an Error is happen :  ', str(e))

    # ----------------------------------------------------------------------------------------
    @staticmethod
    def list_employees():
        try:
            search_results = []
            search_option = input("Do you want to search? (yes/no): ").strip().lower()

            if search_option == "yes":
                search_value = input("Enter name or id of employee:  ").strip()
                for emp in emplyee_list:
                    if emp.emp_id == search_value or emp.name.lower() == search_value:
                        search_results.append(emp)

            sort_option = input("Do you want to sort? (yes/no): ").strip()

            if sort_option == "yes":
                sort_type = input("Enter sort by criteria (emp_id, name, joining_date, salary): ").strip()
                if sort_type in ["emp_id", "name", "joining_date", "salary"]:
                    search_results.sort(key=lambda emp: getattr(emp, sort_type))

            for emp in search_results:
                print(f"ID: {emp.emp_id}, Name: {emp.name}, Joining Date: {emp.joining_date}, Salary: {emp.salary}")

        except ValueError as e:
            print('There is an Error is happen : ', str(e))
        except Exception as e:   # handle any Exception of any type
            print('There is an Error is happen :  ', str(e))

    @staticmethod
    def isFound(id):
        for emp in emplyee_list:
            if emp.emp_id == id:
                return True
        return False
# ------------------------------------------------- *** ----------------------------------------------
def menu():
    while True:
        print('\n')
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        try:
            choice = input("Please ,, Enter your choice here:  ")

            if choice == '1':
                name = str(input("Enter Employee Name: "))
                salary = float(input("Enter Salary: "))
                Employees.create_Employee({"name" : name , "salary" : salary})

            elif choice == '2':
                id = int(input("Enter The Employee id: "))
                if Employees.isFound(id):
                    name = str(input("Enter Employee Name: "))
                    salary = float(input("Enter Salary: "))
                    Employees.update_Employee_data(id ,{"name" : name , "salary" : salary})

            elif choice == '3':
                id = int(input("Enter The Employee id:  "))
                Employees.delete_Employee(id)

            elif choice == '4':
                Employees.list_employees()

            elif choice == '5':
                print("Finish the program. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError as e:
            print('There is an Error is happen : ', str(e))
        except Exception as e:   # handle any Exception of any type
            print('There is an Error is happen :  ', str(e))
# ---------------------------------   ***  ------------------------------------


# <<<<<<<<<<<<<<<<<<<<<<<<<<  Start The Program  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    print("\t\t<<< Employees Management System >>>")
    print("\t\t ===============================")
    menu()  # calling the menue FUN. to execute the tasks.
# <<<<<<<<<<<<<<<<<<<<<<<<<<  End The Program  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>