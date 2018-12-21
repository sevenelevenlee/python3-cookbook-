# -*- coding: utf-8 -*-
'''
问题：实现一个键对应多个值的字典

解决方案：将多个值放到另外的容器中
      d = {
          'a' : [1, 2, 3],
          'b' : [4, 5]
          }
      e = {
          'a' : {1, 2, 3},
          'b' : {4, 5}
          }
使用colletions模块的defaultdict来构造
'''
from collections import defaultdict
# 使用list
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

# 使用set
s = defaultdict(set)
s['a'].add(1)

# 不使用defaultdict, 自己实现
l = {}
for k, v in mydict:
  if k not in l:
    l['k'] = []
  l['k'].append(v)
