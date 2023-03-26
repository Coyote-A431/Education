import re
# tst = test()

r = input()
match = re.fullmatch('[0-9\\.]+', r)
print('yes' if match else 'no')
print(r.isdigit())



