#!/user/bin/env python2
# coding=gbk
#模块
"this is a testmodule"
__author__ = "jimmy chen"

import io
import sys

print sys.getdefaultencoding()


def test():
    args = sys.argv
    if len(args) == 1:
        print "hello,world!"
    elif len(args) == 2:
        print "hello,%s!" % args[1]
    else:
        print "too many arguments"


if __name__ == '__main__':
    test()


class Student(object):

    count = 0

    def __init__(self, name, score=0):
        self.__name = name
        self.__score = score
        Student.count = Student.count + 1
        self._height = 1.68

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    def print_score(self):
        print "%s:%d" % (self.__name, self.__score)


# 测式:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print("测试失败!")
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试成功!')

jim = Student("jim", 99)
jim.__name = "jimmy"
jim.score = 99
print hasattr(jim, "__name")
setattr(jim, "__name", "lucy")

jim.print_score()
print jim.__name
print hasattr(jim, "print_score")
print_score = getattr(jim, "print_score")
print_score()
jim._height = 1.7
print jim._height
