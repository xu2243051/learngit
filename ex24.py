#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex24.py
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

print "Let's practise everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newline and \t tabs'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion form intuition
and requires and explanation
\n\t\twhere there is noe.
"""
print "-------------------"
print poem
print "-------------------"

five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point /=10
print "We can also do that this way"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
