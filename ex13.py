#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex13.py
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

from sys import argv
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
