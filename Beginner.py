# coding=utf-8

# 文字列
text = 'Alice' + 'Bob'
print text

# 数値
text = 4 + 5
print text

# 文字列変換
text = str(4) + str(5)
print text

# 数値リスト
list = [1, 5, 2, 4]
print list

# 文字列リスト
list = ['A', 'B', 'C', 'D']
print list

# 混合リスト
list = ['A', 'B', 3, 4]
print list

print list[1]
print list[-1]
print list[:2]
print list[2:]
print len(list)

# リスト要素削除
del list[1]
print list

list = list + ['B', 'C', 'D']
print list

# ループ
for i in range(5):
    print i

# リストループ
for i in list:
    print i

# インデックスリストループ
for i in range(len(list)):
    print i, list[i]

# リスト内検索
print 'A' in list
print 'B' in list
print 100 not in list
print 'D' not in list

# リスト代入方法
dataA = list[0]
dataB = list[1]
dataC = list[2]
print dataA, dataB, dataC

dataA, dataB, dataC = list[3:]
print dataA, dataB, dataC

# リストインデックス検索
print list.index('A')
print list.index('D')

