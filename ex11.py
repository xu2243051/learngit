#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex11.py
#   创 建 者：许培源
#   创建日期：2014年12月04日
#   描    述：
#
#   更新日志：
#
#================================================================
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print "How old are you ?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you you weigh?",
weight = raw_input()
name = raw_input("What's your name? ")

print "So, you're %r old, %r tall and %r heavy." %(
        age, height, weight)
print "Your name is %s" % name
