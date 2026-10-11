
elog_status = True

ename = input("enter emp name:")
eage = input(f"enter {ename} age:")
ecost = input(f"enter {ename} basic salary:")

tax = float(ecost) * 0.18
gs = tax + float(ecost)

print(f''' emp name:{ename})
{ename} age is :{eage}
{ename} basic salary is :{ecost}
Tax is :{tax}
{ename} Log status is :{elog_status}
tot salary is :{gs}''')