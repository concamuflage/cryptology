def decimal_to_binary(length,int):
    """
    converts a decimal number to a string of 1's and 0's, with length specified by the argument length.
    :param n: an integer
    :param int: an integer
    :return: the binary presentation of the integer that is n bit long.
    """
    binary_string = bin(int)[2:].zfill(length)
    return binary_string