
import re
S = ['120GB', '256GB', '512GB']

tot = 0

for var in S:
    size = re.sub('[A-Za-z]', '', var)
    tot += int(size)

print(f' Sum of {S} disk size is : {tot} gb\n')

print([re.sub('[A-Za-z]', '', var) for var in S])

