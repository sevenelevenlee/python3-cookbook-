# -*- coding: utf-8 -*-
'''
问题： 可迭代对象元素个数超过变量个数时，会抛出ValueError

解决方案： 使用python的星号来出来，星号可以放在首位置、中间位置以及末尾

*可以赋值取出列表的一部分，也可以实现多参数的直接传值
'''
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# 参数时候的使用
records = [('foo', 1, 2), 
           ('bar', 'hello'), 
           ('foo', 3, 4)]

def foo(x, y):
  print('foo', x, y)

for tag, *args in records:
  if tag == 'foo':
    foo(*args) #星号传递参数, args = [1,2], 
  elif tag == 'bar':
    pass

