from task1 import func1
from task1 import func2
from task1 import func3
from task1 import func4
def runner(*function):
    if len(function) == 0:
        func1()
        func2()
        func3()
        func4()
    else:
        for i in function:
            globals()[i]()
runner()