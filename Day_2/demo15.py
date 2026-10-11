


emp = ['101, john, sales, 1000', '102, ram, prod, 20000', '103, raju, hr, 3000', '104, bibu, sales, 4000']

tot = 0
for var in emp:
    if 'sales' in var:
        eid,ename,edept,ecost = var.split(', ')
        print(f"emp name:{ename.title()}\t emp dept:{edept.upper()}")
        tot += int(ecost)
print(f"Total sal: {tot}") 