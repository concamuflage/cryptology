from EuclideanAlgo import euclidean
from fast_expo_modulo import fast_expo_modulo
from ExtendedEuclidean import extended_euclidean_2
from factor_into_two_primes import factor_into_two_primes

def rsa_enrypt(public_key, plaintext):
    """

    :param public_key: a tuple (n,e) tat presents the public key. e is the public exponent and n is the large number.
    :param plaintext: int,
    :return:
    """
    num = public_key[0]
    public_expo = public_key[1]
    # check if plaintext is relatively prime to num
    gcd = euclidean(plaintext,num)
    if gcd != 1:
        raise Exception("Error: plaintext must be an integer that is relatively prime to n in public_key")
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
    #  if private_expo is negative , make it positive.
    while private_expo < 0:
        private_expo += phi
    # if private_expo > phi, make it smaller than phi
    private_expo = (private_expo) % phi

    return (num, private_expo)

def rsa_private_key_generate_given_only_n(public_key):
    """
    this function tries to generate the private key without knowing p, q in n = pq.
    this function works when n in public_key is small
    :param public_key: tuple of integers (n,public_expo)
    :return: private_key: tuple (n, private_expo)
    """
    num = public_key[0]
    prime_p, prime_q = factor_into_two_primes(num)
    return rsa_private_key_generator(public_key,prime_p,prime_q)



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

def rsa_decrypt_without_private_key(public_key, ciphertex):
    """
    first use public key to generate a privatekey and then decrypt the ciphertex
    :param public_key: a tuple (int, int) where the second number is the public exponent
    :param ciphertex: int
    :return: int plaintext,
    """
    private_key = rsa_private_key_generate_given_only_n(public_key)
    plaintext = rsa_decrypt(private_key,ciphertex)

    return plaintext

if __name__ == "__main__":
    print(rsa_private_key_generate_given_only_n((15943,3)))









    
    
    
