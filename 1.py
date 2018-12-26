def prime_num(number):
    """
    function for checking number is prime or not

    :param number: num
    :return:  if number is prime return True,else return False
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def factors_num(number):
    """
    function for find all factors of given number
    :param number:  num
    :return:  list of factors
    """
    fact_list = []
    for i in range(1, number+1):
        if number % i == 0:
            fact_list.append(i)
    return fact_list


def prime_factors(number):
    """
    function for find all prime factors
    :param number:  num
    :return:  list of prime factors
    """
    prime_list = []
    list_l = factors_num(number)
    for i in list_l:
        if prime_num(i) is True:
            prime_list.append(i)
    return prime_list


if __name__ == '__main__':
    num = int(input('Enter the number :'))
    if num <= 0:
        print('None')
    elif prime_num(num) is True:
        print('Number {} is prime'.format(num))
    elif prime_num(num) is False:
        print('Number {} is not prime'.format(num))
    """ loop for display factors  """
    print('Factors are:')
    for j in factors_num(num):
        print(j)
    print("prime factors:")
    """ loop for display all prime factors """
    for j in prime_factors(num):
        print(j)
