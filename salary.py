class Salary:
    def __init__(self):
        self.salaries={}                                    # created object

    def set_emp_salary(self,emp_id,amount):
        self.salaries[emp_id] = amount                        # adding properties into object as key, value pair with bracket notation

    def get_emp_salary(self,emp_id):
          return self.salaries.get(emp_id,"No salary assigned")
