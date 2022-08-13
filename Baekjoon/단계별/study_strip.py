import sys

# strip(), rstrip(), lstrip()
str = " ..Today is Thursday.. "

print('1')
print('\''+str.strip()+'\'')
print('\''+str.rstrip()+'\'')
print('\''+str.lstrip()+'\'')

print('\n2')
print('\''+str.strip('.')+'\'')
print('\''+str.rstrip('.')+'\'')
print('\''+str.lstrip('.')+'\'')

print('\n3')
print('\''+str.strip(' .')+'\'')
print('\''+str.rstrip(' .')+'\'')
print('\''+str.lstrip(' .')+'\'')

print('\n4')
print('\''+str.strip('.Ty')+'\'')
print('\''+str.rstrip('.Ty')+'\'')
print('\''+str.lstrip('.Ty')+'\'')

print('\n5')
print('\''+str.strip(' .Ty')+'\'')
print('\''+str.rstrip(' .Ty')+'\'')
print('\''+str.lstrip(' .Ty')+'\'')


# rstrip('\n')
print('\n\n1')
a1 = sys.stdin.readline()
b1 = sys.stdin.readline()
c1 = sys.stdin.readline()

print(a1, b1, c1)

print('\n2')
a1 = sys.stdin.readline().rstrip('\n')
b1 = sys.stdin.readline().rstrip('\n')
c1 = sys.stdin.readline().rstrip('\n')

print(a1, b1, c1)