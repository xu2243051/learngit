#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex10.py
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

tabby_cat = "\tI'm tabbed in ."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\v* Cat food
\v* Fishes
\v* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

escape_double_quote = " test \""
escape_single_quote = ' escape \''
print '%r' % escape_double_quote
print '%r' % escape_single_quote
print '%s' % escape_double_quote
print '%s' % escape_single_quote
