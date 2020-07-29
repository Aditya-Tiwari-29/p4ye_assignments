import re

fhand=open('regex_sum_766219.txt')
print(sum([float(x) for x in re.findall('[0-9]+',fhand.read())]))

print(change)
