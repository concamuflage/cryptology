from EuclideanAlgo import euclidean
from fast_expo_modulo import fast_expo_modulo
from ExtendedEuclidean import extended_euclidean_2

def rsa_enrypt(public_key, plaintext):
    """
    :param public_key: a tuple (n,e) that presents the public key. e is the public exponent and n is the large number.
    :param plaintext: int,
    :return:
    """
    num = public_key[0]
    public_expo = public_key[1]

    # check if  1 <plaintext<n
    if plaintext <= 1 or plaintext >= num :
        raise Exception("Error: plaintext must be in the range 1 <plaintext<num")
    # encrypt the plaintext
    ciphertext = fast_expo_modulo(plaintext,public_expo,num)
    return ciphertext


def rsa_private_key_generator(public_key, prime_p, prime_q):
    """
    to generate private_key
    :param public_key: a tuple of integers, that is (n,e)
    :param prime_p: prime number
    :param prime_q: prime number
    :return: a tuple (number,private exponent)
    """

    num = public_key[0]
    public_expo = public_key[1]

    # find phi:
    phi = (prime_p - 1)*(prime_q - 1)
    # calculate the private exponent
    private_expo = extended_euclidean_2(public_expo, phi)[0]
    # if private_expo > phi, make it smaller than phi
    private_expo = (private_expo) % phi

    return (num, private_expo)




def rsa_decrypt(private_key,ciphertext):
    """
    :param privatec_key: a tuple (int, int) where the second number is the private exponent
    :param ciphertext: int
    :return: an integer that is the plaintext of ciphertext
    """
    num = private_key[0]
    private_expo = private_key[1]
    plaintext = fast_expo_modulo(ciphertext,private_expo,num)

    return plaintext


# if __name__ == "__main__":
#     pass









    
    
    
