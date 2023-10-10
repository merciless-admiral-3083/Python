import datetime # this will be used below for knowing whether its weekday or not on a given date

class Employee: #we created a class named employee, self means defining itself
    increment = 2 #ab humne kya kara hai ki, hume kisi ki salary ko 2x karna hai

    def __init__(self, fname, lname, salary): #def __init__(self) is mandatory mentioning, followed by details we need of person
        self.fname = fname #self. is reqd, fname here we defined stands for first name
        self.lname = lname #last name
        self.salary = salary

    def increase(self):
        self.salary = self.salary * Employee.increment  # this will search in employee class, we mentioned increment under employee so we must use this
 # self.salary= self.salary * self.increment # self.increment means we are searching in def __init...
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    @classmethod
    def from_string(cls, emp_str): #cls means class, emp_str means emp_str_1 and emp_str_2
        first, last, salary = emp_str.split('-') #we have to retrieve info seperated by - below
        return cls(first, last, int(salary)) #we need theese things

    @staticmethod
    def is_workday(day):
        # Monday is 0, Tuesday is 1, ..., Sunday is 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_str_1 = 'Harry-Jackson-40000'
emp_str_2 = 'Rohan-Das-40000'

Emp_1= Employee('Harry', 'Jackson', 40000) #Now we need not to do a= Harry, b= Jackson Salary=40000, but we can do this form
Emp_2= Employee('Rohan', 'Das', 40000) #same here

print(Emp_1.fullname()) #by this  we just need to mention Emp1 or Emp2 to get the name

print(Emp_1.fname, Emp_2.fname) #Emp_1 is Emp_1 defined in 2nd last line, fname refers to the data we input in __init__(self,fname...)

print(Emp_1.salary) #salary before increment

Emp_1.increase() #we increaseed salary here

print(Emp_1.salary) #this will print increaseed salary

new_emp_1 = Employee.from_string(emp_str_1)  #we just mentioned the thing which we can type to print the data we want like we do c= a+b where a and b were already defined

print(new_emp_1.salary) #this will print salary
print(emp_str_1)

print(new_emp_1.fullname()) #by this  we just need to mention Emp1 or Emp2 to get the name

print(new_emp_1.fname)  # Accessing the first name of Employee 1

print(new_emp_1.salary)  # Salary before increment

new_emp_1.increase()  # Increase salary

print(new_emp_1.salary)  # Salary after increment

my_date = datetime.date(2023, 9, 26)

print(Employee.is_workday(my_date))
