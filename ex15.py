#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex15.py
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

# import features from module sys
from sys import argv

# get filename from arguments
script, filename = argv

# open a file for reading
txt = open(filename)

# print a line 
print "Here's my file %r:" % filename
# print content which is read from file
print txt.read()
txt.close()

# prompt to input the filename again
print "I'll also ask you to type it again:"
# input filename , and assign it to file_again
file_again = raw_input('> ')

# open the file, and assign file object to txt_again
txt_again = open(file_again)

# use read to read the content of file
print txt_again.read()
txt_again.close()
