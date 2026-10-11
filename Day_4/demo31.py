
fobj = open('C:\\Users\\Admin\\emp.csv', 'r')
L = fobj.readlines()
fobj.close()

tot = 0
for var in L:
    if 'sales' in var:
        emp_list = var.split(",")
        ecost = emp_list[-1]
        tot = tot + int(ecost)
print(f"sum of sales dept emp's cost :{tot}")

