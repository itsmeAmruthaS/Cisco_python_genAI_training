wobj = open("r1.log", "w")
wobj.write("sample data\n")
wobj.write("prod name is : pA cost is : 4565\n")
pname = 'p8'
pcost = 35523.23
wobj.write(f'prod name is :{pname} cost is:{pcost}\n')
wobj.write('-----------------------------')
wobj.close()