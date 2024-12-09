def fast_exponentiation(root, power):
    """
    for calculating root^power with fast exponentiation
    root:int
    power: int
    return an int
    """
    # special case
    if power == 0:
        return 1
    return fast_exponentiaion_helper(root,power,1)
    

def fast_exponentiaion_helper(root,power,accumulator):
    if power == 0:
        return accumulator
    if (power % 2 == 1): # if the power is odd
        return fast_exponentiaion_helper(root,power-1,root*accumulator)
    else: 
        return fast_exponentiaion_helper(root*root,power // 2,accumulator)
# if __name__ == "__main__":
#     print(fast_exponentiation(539704,131))