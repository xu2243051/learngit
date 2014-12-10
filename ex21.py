#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex21.py
#   创 建 者：许培源
#   创建日期：2014年12月08日
#   描    述：
#
#   更新日志：
#
#================================================================
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d"  %(a, b)
    return a / b

print "Let's do some math with just funcitons!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height %d, Weight %d, IQ:%d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print "That becomes: ", what, "Can you do it by hand"
