
import re
fname = input("Enter file name: ")

reg_file = open(fname)
lst = []
sum = 0
for line in reg_file:
    temp = re.findall('[0-9]+', line)
    for x in temp:
        lst.append(x)
for num in lst:
    sum = sum + int(num)
print (sum)