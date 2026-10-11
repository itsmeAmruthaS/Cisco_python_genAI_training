

fobj = open('C:\\Users\\Admin\\Documents\\Training\\Day_3\\emp.csv', "r")
s = fobj.read()
fobj.close()

print(type(s), len(s))
print("")
print("display file content")
print(s)