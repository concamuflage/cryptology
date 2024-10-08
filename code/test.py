def find_x():
    """returns a x such that x*83 is a multiple of 103"""
    for num1 in range(1,10000):
        for num2 in range(1,num1*103):
            if num2*87 == 103*num1:
                return num2
print(find_x())