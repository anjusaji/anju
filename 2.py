def fibonacci(number):
    """
    function for calculate fibonacci sereies
    :param number: num
    :return: fibonacci series

    """
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)


if __name__ == '__main__':
    num = int(input('Enter the number :'))
    print('fibonacci series are')
    for i in range(num):
            print(fibonacci(i))
