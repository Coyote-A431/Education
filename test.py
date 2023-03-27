import re
import os
# tst = test()

# r = input()
# match = re.fullmatch('[0-9\\.]+', r)
# print('yes' if match else 'no')
# print(r.isdigit())

# f = '\n'
# a = f.strip()
# print(a)

with open(r'C:\Users\Unknown\Desktop\Education\Animal\jopa.txt', 'r', encoding='utf-8') as test, \
        open(r'C:\Users\Unknown\Desktop\Education\Animal\pizda.txt', 'w', encoding='utf-8') as ed:
    for line in test:
        if line != '':
            ed.write(line)

# with open(r'C:\Users\Unknown\Desktop\Education\Animal\jopa.txt', 'r') as test:
#     test.writelines(lines)

