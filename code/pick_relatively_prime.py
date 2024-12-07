import random
from EuclideanAlgo import euclidean
def pick_relatively_prime(int):
    """
    randomly pick a number that is coprime to int and less than int.
    :param int: integer
    :return: a number less than in and is cooprime to int.
    """
    while True:
        rand = random.randint(1,int)
        if euclidean(rand,int) == 1:
            return rand

if __name__=="__main__":
    print(pick_relatively_prime(54959*33107))
