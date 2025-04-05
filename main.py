from employee import Employee
from department import Department
from salary import Salary




def main():

    # create departments
    dept1 = Department("IT")
    dept2 = Department("HR")

    # create employees
    emp1 = Employee(1,"Mouni",dept1.get_dept_name())
    emp2 = Employee(2, "Mahi",dept2.get_dept_name())

    # Manage salaries 
    sal = Salary()
    sal.set_emp_salary(emp1.emp_id,25000)
    sal.set_emp_salary(emp2.emp_id,80000)

    # print details 
    print(emp1.get_emp_details())
    print("Salary:",sal.get_emp_salary(emp1.emp_id))
    print("-----------------------------------------------------------")
    print(emp2.get_emp_details())
    print("Salary:",sal.get_emp_salary(emp2.emp_id))
    

if __name__ == "__main__":
    main()
    