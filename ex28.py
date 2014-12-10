#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex28.py
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

print  True and True
print  False and True
print  1 == 1 and 2 == 1
print  "test" == "test"
print  1 == 1 and 2 != 1
print  True and 1 == 1
print  False and 0 != 0
print  True or 1 == 1
print  "test" == "testing"
print  1 != 0 and 2 == 1
print  "test" != "testing"
print  "test" == 1
print  not (True and False)
print  not (1 == 1 and 0 != 1)
print  not (10 == 1 or 1000 == 1000)
print  not (1 != 10 or 3 == 4)
print  not ("testing" == "testing" and "Zed" == "Cool Guy")
print  1 == 1 and not ("testing" == 1 or 1 == 0)
print  "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print  3 == 3 and not ("testing"  == "testing" or "Python" == "Fun")
