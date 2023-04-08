from sys import path

path.append(".//modules")

for p in path:
    print(p)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))


a = "AaBbCc StrinGa"
ordlist = []
for char in a:
    ordlist.append(str(ord(char)))
    ordlist.append("-")

print(ordlist)
# b = "".join(ordlist)
# print(b.split("-"))
b = "".join([chr(int(c)) for c in ordlist if c != "-"])

print(a)
print(b)
print(b == a)

multiline = '''Line #1
Line #2'''

print(len(multiline))

