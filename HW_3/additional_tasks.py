import re
from collections import Counter
from math import trunc


# Task #1
def convert_n_to_m(x=None, n=10, m=2, in_list_of_digits=False):
    """
    Converts integral number in 'n' base to it's representation in 'm' base
    :param x: input number (None, by default)
    :param n: input base (10, by default)
    :param m: output base (2, by default)
    :param in_list_of_digits: output type (list if True, str if False)
    :return: 'x' number with a new base ('m')
    """
    large_base = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
        18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
        26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
        34: 'Y', 35: 'Z'
    }
    n = int(n)
    m = int(m)
    digits = list()

    if ((type(x) is not str) and
            (type(x) is not int) or any([
                (n < 1), (m < 1),
                (n > 36), (m > 36)
            ]) or not x):
        return False

    if x == 0:
        return [0]

    try:
        x = int(str(x), n)
        if m == 1:
            return str().join('0' for _ in range(x))
    except ValueError:
        return False

    if m == 2:
        digits = list("{0:b}".format(x))
    elif m == 8:
        digits = list("{0:o}".format(x))
    elif m == 16:
        digits = list("{0:x}".format(x).upper())
    else:
        while x:
            digits.append(int(x % m))
            x //= m  # x /= m - for python2
        digits = digits[::-1]
        digits = [large_base[n] if n > 9 else n for n in digits]

    return digits if in_list_of_digits else str().join([str(d) for d in digits])


# Task #2
def find_most_frequent(text: str) -> list:
    """
    Finds the most frequent words in the given text
    :param text: input text of arbitrary length
    :return: list of the most frequent words
    """
    words = re.findall(r"[\w']+", text.lower())
    count = Counter(words)
    largest_occurrence = sorted(count.values(), reverse=True)[0]
    return sorted([key for key in count
                   if count[key] == largest_occurrence])


# Task #3
def my_sort(func=None, array=list(), reversed=False) -> list:
    """
    Custom sort function
    :param func: key-function for sorting (None, by default)
    :param array: one-dimensional array of data of the same type
    :param reversed: reverse output data, if True (False, by default)
    :return: sorted data array in list format
    """
    if any([type(array) is not list,
            type(reversed) is not bool,
            func and not callable(func)]):
        raise TypeError("Incorrect arguments pass: '{f}', '{a}', '{r}'".format(
            f=func,
            a=array,
            r=reversed)
        )
    if func:
        return sorted(array, key=func)
    return sorted(array, reverse=True) if reversed else sorted(array)


# Task 4
def counter(a: int, b: int) -> int:
    """
    Finds common elements in comparison of 2 numbers
    :param a: first non-negative integer
    :param b: second non-negative integer
    :return: a quantity of similar numbers between two numbers
    """
    if type(a) is not int or type(b) is not int:
        raise TypeError("Input values are not 'int'")
    a = set(str(a))
    b = set(str(b))
    return len(a.intersection(b))


# Task 5
def count_holes(n: int or str):
    """
    Counts how much 'holes' is the input number contains
    :param n: an integer number or string that contains an integer number
    :return: quantity of holes that the input number contains
    """
    if type(n) is not int and type(n) is not str:
        return "ERROR: Input value is not 'int' or 'str', but '{}'".format(
            type(n))
    holes = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}
    n = int(n)
    n = abs(n)
    res = 0
    for e in list(str(n)):
        res += holes[int(e)]
    return res


# Task 6
def is_palindrome(data: str or int) -> str:
    """
    Checks if the input data is a palindrome
    :param data: input data in str or int format
    :return: 'YES' if the input data is a palindrome, otherwise - 'NO'
    """
    if type(data) is not str and type(data) is not int:
        return "ERROR: Input value is not 'int' or 'str', but '{}'".format(
            type(data))
    data = str(data).lower().replace(' ', '')
    if len(data) == 1:
        return 'YES'
    res = lambda d: [d[i] == d[len(data) - int(i) - 1]
                     for i in range(trunc(len(d) / 2))]
    return 'NO' if False in res(data) else 'YES'


# Task 7
def is_parenthesis_balanced(exp: str) -> bool:
    """
    Checks if parenthesis are balanced in the string expression
    :param exp: input string expression containing parenthesis
    :return: True/False depending on whether parenthesis are balanced or not
    """
    if type(exp) is not str:
        raise TypeError("Input data is not in str format, '{}' given.".format(
            type(exp)))
    parenthesis = re.sub(r'[a-zA-Z0-9\-+/*%]', '', exp)
    if (parenthesis.startswith(')')
            or parenthesis.count('(') != parenthesis.count(')')):
        return False
    buffer = 0
    for p in parenthesis:
        buffer += 1 if p == '(' else -1
        if buffer < 0:
            return False
    return False if buffer != 0 else True


def main():
    print("Task #1:")
    print(convert_n_to_m([123], 4, 3))     # False
    print(convert_n_to_m("0123", 5, 6))    # 102
    print(convert_n_to_m("123", 3, 5))     # False
    print(convert_n_to_m(123, 4, 1))       # 000000000000000000000000000
    print(convert_n_to_m(-123.0, 11, 16))  # False
    print(convert_n_to_m("A1Z", 36, 16))   # 32E7
    print("-------")
    print()
    print("Task #2:")
    print(find_most_frequent("Hello,Hello, my dear!"))  # ['hello']
    print(find_most_frequent("to understand recursion you need first to understand recursion..."))  # ['recursion', 'to', 'understand']
    print(find_most_frequent("Mom! Mom! Are you sleeping?!!!"))  # ['mom']
    print("-------")
    print()
    print("Task #3:")
    print(my_sort(array=["Aa", "cCc", "bbbbb", "a"]))                           # ['Aa', 'a', 'bbbbb', 'cCc']
    print(my_sort(array=["Aa", "cCc", "bbbbb", "a"], reversed=True))            # ['cCc', 'bbbbb', 'a', 'Aa']
    print(my_sort(func=(lambda x: len(x)), array=["Aa", "cCc", "bbbbb", "a"]))  # ['a', 'Aa', 'cCc', 'bbbbb']
    print("-------")
    print()
    print("Task #4:")
    print(counter(12345, 567))      # 1
    print(counter(1233211, 12128))  # 2
    print(counter(123, 45))         # 0
    print("-------")
    print()
    print("Task #5:")
    print(count_holes('123'))  # 0
    print(count_holes(906))    # 3
    print(count_holes('001'))  # 0
    print(count_holes(-8))     # 2
    print(count_holes(-8.0))   # ERROR
    print("-------")
    print()
    print("Task #6:")
    print(is_palindrome(0))                      # YES
    print(is_palindrome('puppy'))                # NO
    print(is_palindrome('mystring1Gni rts ym'))  # YES
    print("-------")
    print()
    print("Task #7:")
    print(is_parenthesis_balanced("()()((()())))"))          # False
    print(is_parenthesis_balanced(")(())("))                 # False
    print(is_parenthesis_balanced("(a-2)*(sqrt(4x)-6)**2"))  # True
    print("-------")


if __name__ == "__main__":
    main()
