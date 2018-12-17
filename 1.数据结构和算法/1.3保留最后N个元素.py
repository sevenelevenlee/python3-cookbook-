# -*- coding: utf-8 -*-
'''
问题：迭代操作怎么样只保留最后几个有限的元素历史记录

保留有限历史记录正是 collections.deque
deque(maxlen=N)构造一个固定大小的队列，当队列满了的时候，加入新的元素，最老的元素会被移除

队列与列表的区别， 队列在两端插入或删除元素的时间复杂度为O(1)
'''

# 使用deque保存匹配的最后几行
from collections import deque

def search(lines, pattern, history=5):
  previous_lines = deque(maxlen=history)
  for line in lines:
    if pattern in line:
      yield line, previous_lines
    previous_lines.append(line)

if __name__ == '__main__':
  with open(r"somefile.py") as f:
    for line, previous in search(f, 'python', 5):
      for pline in previous:
        print(pline, end='')
      print(line, end='')
