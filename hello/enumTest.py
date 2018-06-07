# coding=utf-8
from enum import Enum
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
print Month.__members__
print "\r\n"
print Month.__members__.items()
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print Month.__members__.items()[3]
print Month[0]