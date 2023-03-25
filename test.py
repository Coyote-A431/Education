import re
# tst = test()

r = input()
match = re.fullmatch('[а-яА-ЯёЁ]+', r)
print('yes' if match else 'no')



