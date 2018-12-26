def prime_num(number):
    """
    function for checking number is prime or not

    :param number: num
    :return:  if number is prime return True,else return False
    loop for display factors  """
    print('Factors are:')
    for j in factors_num(num):
        print(j)
    print("prime factors:")
    """ loop for display all prime factors """
    for j in prime_factors(num):
        print(j)
