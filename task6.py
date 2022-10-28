def high_2(n):
    return (n&(~(n-1)))
n = int(input("введите число:\n"))
print('max делитель(степень 2)\n',high_2(n))
