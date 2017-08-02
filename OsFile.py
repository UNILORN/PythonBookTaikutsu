# coding=utf-8

import os

path = './'
print os.getcwd()

print os.path.getsize(path)
print os.path.isfile(path)
print os.path.isdir(path)

# ファイル読み込み
edit_file = open(path+'test.txt')
print edit_file.read()
edit_file.close()

# ファイル単行読み込み
edit_file = open(path+'test.txt')
print edit_file.readline()
edit_file.close()

# ファイル書き込み
edit_file = open(path+'test.txt','w')
edit_file.write('Hello world\n')
edit_file.close()

# ファイル追記
edit_file = open(path+'test.txt','a')
edit_file.write('hogehoge\n')
edit_file.write('piyopiyo\n')
edit_file.close()

# 変数保存
import shelve

shelf_file = shelve.open('./mydata')
cats = ['Zophie', 'Pooka']
shelf_file['cats'] = cats
shelf_file.close
del shelf_file

# 変数呼び出し
shelf_file = shelve.open('./mydata')
print type(shelf_file)
print shelf_file['cats']
shelf_file.close

