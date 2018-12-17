# -*- coding: utf-8 -*-
#问题： N个元素的元祖或序列（字符串）同时赋值给N个变量
'''
这种解压赋值可以用在任何可迭代对象上面
'''

# 元组
p = (4,5)
x, y = p

# 列表
data = [ 'ACME', 50, 91.1, (2018, 12, 17) ]
name, shares, price, date = data

# 字符串
s = "Hello"
a, b, c, d, e = s
