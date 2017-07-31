# coding=utf-8

# 変数の参照

list = [0, 3, 5, 7, 9]

cheese = list

print list
print cheese

list.append(10)

print list
print cheese

# コピー

import copy

cheese = copy.copy(list)

list.remove(10)

print list
print cheese

