# -*- coding: utf-8 -*-
'''
问题： 数据字典中执行最小值、最大值、排序

解决方案：使用zip() 将键值反转过来
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 最小值
min_price = min(zip(prices.values(), prices.keys()))

# 排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))

#  min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息
key = min(prices, key = lambda k: prices[k])
