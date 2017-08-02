# coding=utf-8

import os

path = './'
print os.getcwd()

print os.path.getsize(path)
print os.path.isfile(path)
print os.path.isdir(path)

edit_file = open(path+'test.txt')
print edit_file.read()