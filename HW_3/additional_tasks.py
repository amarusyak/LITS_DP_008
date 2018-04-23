# Task #1
def number_to_base(x, n=10, m=2, in_list_of_digits=True):
    """
    Converts integral number in 'n' base to it's representation in 'm' base
    :param x: input number
    :param n: input base
    :param m: output base
    :param in_list_of_digits: output type (list if True, str if False)
    :return: 'x' number with a new base ('m')
    """
    if any([
        (n < 2),
        (m < 2),
        (n > 36),
        (m > 36),
        ((type(n) is not str) and
         (type(m) is not str) and
         (type(n) is not int) and
         (type(m) is not int))
    ]):
        return False

    digits = list()

    if x == 0:
        return [0]

    if n != 10 and n != '10':
        x = number_to_base(x, n=n, m=10)

    if m == 2:
        digits = list("{0:b}".format(x))
    elif m == 8:
        digits = list("{0:o}".format(x))
    elif m == 16:
        digits = list("{0:x}".format(x))
    else:
        while x:
            digits.append(int(x % m))
            x /= m
        digits = digits[::-1]

    return digits if in_list_of_digits else ''.join([str(d) for d in digits])
