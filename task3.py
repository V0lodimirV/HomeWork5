"""
nums =[0, 1, 2, 3, 4, 7, 8, 10]
ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
iranges = iter(nums[0:1] + ranges + nums[-1:])
print (', '.join([str(n) + '-' + str(next(iranges)) for n in iranges]))
"""



from itertools import groupby
from operator import itemgetter
data = [0, 1, 2, 3, 4, 7, 8, 10]
for k, g in groupby(enumerate(data), lambda ix: ix[0] -ix[1] ):
    print(list(map(itemgetter(1), g)))