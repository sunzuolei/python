#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'
s = Student('Bob', 59)
print s.grade
s.score = 60
print s.grade
s.score = 99
print s.grade
# 给Student类加一个grade属性，根据 score 计算 A（>=80）、B、C（<60）。