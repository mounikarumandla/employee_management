class Employee:                                                            # defining class
    def __init__(self,emp_id,name,deparment):                              # constructor method
        self.emp_id=emp_id                                                 # instance variable
        self.name=name
        self.deparment=deparment

    def get_emp_details(self):                                                 # instance method
        return f"ID: {self.emp_id} , Name: {self.name} , Department: {self.deparment}"    
