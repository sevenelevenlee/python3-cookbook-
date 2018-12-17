# -*- coding: utf-8 -*-

# 利用 heapq 模块实现了一个简单的优先级队列
import heapq

class PriorityQueue():
  def __init__(self):
    self.queue = []
    self.index = 0
  def push(self, item, priority):
    heapq.heappush(self.queue, (-priority, self.index, item))
    self.index += 1
  def pop(self):
    return heapq.heappop(self.queue)[-1]

'''
队列包含了一个 (-priority, index, item) 的元组。 优先级为负数的目的是使得元素按照优先级从高到低排序
'''
