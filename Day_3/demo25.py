
def file_read():
    fobj = open('r1.log', "r")
    s = fobj.read()
    fobj.close()
    print('file content:')
    print(s)
    print("end of func block")

def calc_sales_cost():
    tot = 0
    for var in [10,20,30,40,50]:
        tot += var
    print(f"total sales cost: {tot}")


print("--this main block")
file_read()
print('')
calc_sales_cost()
print("")
if(True):
    file_read()
print("end of script")