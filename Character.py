# coding=utf-8

# p129
text = 'Hello world .'

long_text = '''
aaa
bbb
ccc
'''
print long_text
print text

# p133

print text[0]
print text[:5]

print text.upper()
print text.lower()
print text[5:].islower()
print text.isupper()

# p138

print text.startswith('Hello')
print text.endswith('world .')

print text.split()
print ' '.join(text)

# p140

print text.rjust(20,'*')
print text.ljust(20,'*')
print text.center(20,'*')
