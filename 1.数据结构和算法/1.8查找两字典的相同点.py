# -*- coding: utf-8 -*-

'''
问题： 寻找两字典中相同的键或值

解决方案：在两字典的keys()和items()返回的结果上执行集合操作, 
        keys(), items()支持集合操作. 
        values() 需要转换成set, 因为不能保证值互不相同
'''

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 相同的key
a.keys() & b.keys() #{'x', 'y'}

# a中存在而b没有的key
a.keys() - b.keys() #{'z'}

# 相同的key和value
a.items() & b.items() #('y', 2)

# 使用dict推导式来处理新的字典
c = {key: a[key] for key in a.keys() - {'w', 'z'}}

