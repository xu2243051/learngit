#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex3.py
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

print "I will not count my chickents."

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"
print 3+2+1-5+4%2-1/4+6 

print "Is it true that 4+2<5-7?"
print 3 + 2 < 5 - 7 # compare

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it is False."

print "How about some more"

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
