#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex20.py
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

from sys import argv

script, input_file = argv

# define a function called print_all, it print the whole file
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

# print one line of file
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First, let's print the whole file:\n"
print_all(current_file)

# come back to the first position of the file
print "Let's rewind, kind of like a tape"
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
#current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
# current_line = current_line + 1
print_a_line(current_line, current_file)
