#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex5.py
#   创 建 者：许培源
#   创建日期：2014年12月03日
#   描    述：
#
#   更新日志：
#
#================================================================
import sys
reload(sys)
sys.setdefaultencoding('utf8')

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
my_height = height * 2.54 # cm
my_weight = weight * 0.454 # kilograms

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Actuall that's not too heavy."
print "He's get %s eyes and %s hair." %(eyes, hair)
print "His teech are usually %s depending on the coffee." % teeth

print "He's %f cm tall." % my_height
print "He's %f kg heavy." % my_weight
# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d. I get %r." %(
        age, height, weight, age+height+weight)
