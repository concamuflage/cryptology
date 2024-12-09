def binary_string_cross_product(binary_vector_1,binary_vector_2):
    """
    a function for computing the following value:
    binary_vector_1[0]*binary_vector_2[0] +
    binary_vector_1[1]*binary_vector_2[1] +
    ...
    binary_vector_1[n-1]*binary_vector_2[n-1]


    :param binary_vector_1:a string
    :param binary_vector_2:a string
    :return:  a string consists of 1's and 0's
    """
    length_1 = len(binary_vector_1)
    length_2 = len(binary_vector_2)
    if length_1 != length_2:
        raise Exception("The length of the vectors are not equal")
    total = 0    # for storing the sum of product
    for index in range(length_1):
        pair_sum = int(binary_vector_1[index])*int(binary_vector_2[index])
        total += pair_sum

    return total % 2