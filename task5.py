from math import log
n = int(log(int(input('введите число:\n')),2))
print(n)
num = 1
for i in range(n):
    num = num*2
print(num)
