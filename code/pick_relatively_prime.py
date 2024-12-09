import random
from EuclideanAlgo import euclidean
def pick_relatively_prime(int):
    """
    for picking a random number that is coprime to int and less than int.
    :param int: an integer
    :return: a number less than in and is coprime to int.
    """
    while True:
        rand = random.randint(1,int)
        if euclidean(rand,int) == 1:
            return rand

# if __name__=="__main__":
#     print(pick_relatively_prime(54959*33107))
