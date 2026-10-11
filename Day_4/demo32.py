
class Enrollment:
    def __init__(self,n,d,p):
        self.name = n
        self.dob = d
        self.place = p
        print(f'emp {self.name} enrollment done')

    def display(self):
        print(f'About {self.name} details:')
       
        print(f'Name: {self.name} dob: {self.dob} place: {self.place}')

obj1 = Enrollment('John Doe', '1st jan', 'New York')
obj2 = Enrollment('Jane Smith', '2nd feb', 'Los Angeles')

obj1.display()
obj2.display()