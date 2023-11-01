"""
Imagine you have a call center with three levels of employees: respondent, manager,
and director. An incoming telephone call must be first allocated to a respondent who is free. If the
respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
free or not able to handle it, then the call should be escalated to a director. Design the classes and
data structures for this problem. Implement a method dispatchCall() which assigns a call to
the first available employee.

Notes:
CallCenter: respondent, manager, director
    -data structure:
    {employee type: [employee, ...],
     ...
    }

    -add

    -dispatchCall():
        -assigns a call ot the first available employee
        -incoming call => free respondent => manager => director
"""

class CallCenter:
    def __init__(self):
        """ Stores nodes """
        self.employees = {'Respondent':[],
                          'Manager':[],
                          'Director':[]}
        
    def add_employee(self, employee, position, employer):
        """ Input: employee = str, position = respondent/manager/director"""
        if position == 'Respondent':
            new_employee = Respondent(employee, employer)
            if new_employee not in self.employees['Respondent']:
                return self.employees['Respondent'].append(new_employee)
            return print('Employee already in roster')
        elif position == 'Manager':
            new_employee = Manager(employee, employer)
            if new_employee not in self.employees['Manager']:
                return self.employees['Manager'].append(new_employee)
            return print('Employee already in roster')
        elif position == 'Director':
            new_employee = Director(employee, employer)
            if new_employee not in self.employees['Director']:
                return self.employees['Director'].append(new_employee)
            return print('Employee already in roster')
        
    def see_employees(self):
        for position, employee_list in self.employees.items():
            for employee in employee_list:
                print(f'Position: {position}, Employee: {employee}, Hold: {employee.hold}, Call: {employee.call}')
        

    def dispatchCall(self):
        # Iterate through self.employees to find who is not on a call
        # Once first employee not on a call is found switch self.hold to True
        for position, employee_list in self.employees.items():
            for employee in employee_list:
                if employee.hold == False:
                    employee.hold = True
                    return print(f'call transfered to {employee}')
        return print('Call unable to be transfered')
        
        
class Employee:
    def __init__(self, name, employer):
        self.name = name
        self.position = None
        self.employer = employer
        self.hold = False
        self.call = False
        
    def __str__(self):
        return f'{self.name}'

    def pick_up(self):
        if self.hold == True:
            self.call = True

    def hang_up(self):
        if self.hold == True and self.call == True:
            self.hold = False
            self.call = False

    def escalate(self):
        position = self.position
        if position == 1:
            for employee in self.employer.employees['Manager']:
                if employee.hold == False:
                    employee.hold = True
                    self.hang_up()
                    return print(f'call transfered from {self} to {employee}')
            for employee in self.employer.employees['Director']:
                if employee.hold == False:
                    employee.hold = True
                    self.hang_up()
                    return print(f'call transfered fron {self} to {employee}')
        else:
            return ('Call unable to be transfered')
        if position == 2:
            for employee in self.employer.employees['Director']:
                if employee.hold == False:
                    employee.hold = True
                    self.hang_up()
                    return print(f'call transfered from {self} to {employee}')
        else:    
            return print('Call unable to be transfered')
        


class Respondent(Employee):
    def __init__(self, name, employer):
        super().__init__(name, employer)
        self.position = 1


class Manager(Employee):
    def __init__(self, name, employer):
        super().__init__(name, employer)
        self.position = 2

class Director(Employee):
    def __init__(self, name, employer):
        super().__init__(name, employer)
        self.position = 3


# Testing:
call_center = CallCenter()
call_center.add_employee('1', 'Respondent', call_center)
call_center.add_employee('2', 'Respondent', call_center)
call_center.add_employee('3', 'Respondent', call_center)
call_center.add_employee('4', 'Manager', call_center)
call_center.add_employee('5', 'Manager', call_center)
call_center.add_employee('6', 'Manager', call_center)
call_center.add_employee('7', 'Manager', call_center)
call_center.add_employee('8', 'Director', call_center)
# call_center.see_employees()
call_center.dispatchCall()
employee1 = call_center.employees['Respondent'][0]
employee1.pick_up()
call_center.dispatchCall()
call_center.dispatchCall()
employee2 = call_center.employees['Respondent'][1]
employee1.hang_up()
employee2.pick_up()
employee2.escalate()
call_center.see_employees()

