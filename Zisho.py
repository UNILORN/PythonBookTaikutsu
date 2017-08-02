# coding=utf-8
import pprint

# p109 辞書とデータ構造

zisho = {'size': 'big', 'color': 'gray'}
print zisho['size']

# p110 比較

spam = {'color': 'gray', 'size': 'big'}

print spam == zisho

# p112 メソッド

print zisho

print zisho.values()
print zisho.keys()
print zisho.items()

# p114 setdefault

print zisho
zisho.setdefault('spec', 4)
print zisho
zisho.setdefault('color', 'green')  # 既にセットされているため変更されない
print zisho

# p115 characterCount

message = 'Between 1987 and 1993, a significant delay occurred in the release of the new version of GNU Emacs (which should be version 19) [3]. In the late 1980s, Lucid of Richard P. Gabriel was facing the need to release Emacs to support the Energize C ++ IDE. Therefore, Lucid recruited a team to improve and extend the Emacs code [4], a new version of Lucid, released in 1991, intended to form the basis of version 19 of GNU Emacs It was made. However, Lucid was not able to afford to wait for the Free Software Foundation (FSF) to accept this change [5]. Lucid continued developing and maintaining its own version of Emacs, but one year later FSF merged some Lucid version code and released version 19 of GNU Emacs incorporating other parts as well [6].'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

