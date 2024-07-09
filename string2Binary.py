import sys

value1 = sys.argv[1]

binary = ''.join(format(ord(x), '08b') for x in value1)

print(binary)