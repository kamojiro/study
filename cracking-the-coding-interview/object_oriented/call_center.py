from collections import deque

# TODO 飽きた

class Caller:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, rank):
        self.name = name
        self.current_call = None
        self.rank = rank
    def receive_call(self):
        pass
    def call_complete(self):
        call = self.current_call
        self.current_call = None
        return call
    def assign_call(self, call):
        self.current_call = call

class Director(Employee):
    def __init__(self, name):
        super.__init__(name, "director")

class Manager(Employee):
    def __init__(self, name):
        super.__init__(name, "manager")

class Respondent(Employee):
    def __init__(self, name):
        super.__init__(name, "respondent")


class Call:
    def __init__(self, caller):
        self.caller = caller
        self.minimum_rank = None
        self.employee = None
    
    def set_rank(self, rank):
        self.minimum_rank = rank

    def assign_employee(self, employee):
        self.employee = employee
    
    def assigned_employee(self):
        return self.employee

class CallHandler:
    def __init__(self):
        # 0 -> respondent
        # 1 -> manager
        # 2 -> director
        self.call_queue = [ deque() for _ in range(3)]
        self.free_employee = [ deque() for _ in range(3)]
        self.employee = [[] for _ in range(3)]
    
    def set_call(self, call):
        if call.rank == "respondent":
            self.call_queue[0].append(call)
        elif call.rank == "manager":
            self.call_queue[1].append(call)
        elif call.rank == "director":
            self.call_queue[2].append(call)
    
    def set_employee(self, employee):
        if employee.rank == "director":
            self.free_employee[0].append(employee)
        elif employee.rank == "manager":
            self.free_employee[1].append(employee)
        elif employee.rank == "respondent":
            self.free_employee[2].append(employee)
    
    def assign_call(self):
        for i in reversed(range(len(self.call_queue))):
            while self.call_queue[i]:
                call = self.call_queue[i]
                assigned = False
                for j in range(i, len(self.free_employee)):
                    if self.free_employee[j]:
                        employee = self.free_employee[j].popleft()
                        call.assign_employee(employee)
                        employee.assign_call(call)
                        assigned = True
                        break
                if not assigned:
                    break

def test():
    call_handler = CallHandler()
    employees = []
    for i in range(1,3):
        director = Director("d" + "str1")
        call_handler.set_employee(director)
        employees.append(director)
    for i in range(1,5):
        manager = Manager("m" + "str1")
        call_handler.set_employee(manager)
        employees.append(manager)
    for i in range(1,7):
        respondent = Respondent("r" + "str1")
        call_handler.set_employee(respondent)
        employees.append(respondent)
    for i in range(14):
        call = Call("caller"+str(i))
        if i%3 == 0:
            call.set_rank("director")
        elif i%3 == 1:
            call.set_rank("manager")
        elif i%3 == 2:
            call.set_rank("respondent")
        call_handler.set_call(call)
    call_handler.assign_call()
    







