from .application.db import people
from .application import salary

import datetime

if __name__ == '__main__':
  print('Успешно выполнено с помощью salary.py')

vremya = datetime.datetime.now()
print(vremya)

print(people)
print(salary)