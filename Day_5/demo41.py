
print('welcome')
print('test 1')
print('test 2')
print('test 3')

try:
    print('welcome')
except Exception as eobj:
    print(eobj)
else:
    print('No exception occurred')
finally:
    print('running')

for var in range(5):
    print(var)
    print("-"*10)

tot = 10+20
print(tot)

