#!/usr/bin/python
#coding:utf-8
#================================================================
#   Copyright (C) 2014 All rights reserved.
#   
#   文件名称：ex7.py
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

# 玛丽有一只小羊羔
print "Mary had a little lamb."
# 它的绒毛白如雪
print "Its fleece was white as %s." % 'snow'
# 跟着玛丽到处跑
print "And everywhere that Mary went."
# 打印10个 . 
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happen
# print Cheese
print end1 + end2 + end3 + end4 + end5 + end6,
# print Burger
print end7 + end8 + end9 + end10 + end11 + end12
