import re
from collections import Counter


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
    counter = Counter(words)
    largest_occurrence = sorted(counter.values(), reverse=True)[0]
    return sorted([key for key in counter
                   if counter[key] == largest_occurrence])


def main():
    print("Task #1")
    print(convert_n_to_m([123], 4, 3))     # False
    print(convert_n_to_m("0123", 5, 6))    # 102
    print(convert_n_to_m("123", 3, 5))     # False
    print(convert_n_to_m(123, 4, 1))       # 000000000000000000000000000
    print(convert_n_to_m(-123.0, 11, 16))  # False
    print(convert_n_to_m("A1Z", 36, 16))   # 32E7
    print("-------")
    print()
    print("Task #2")
    print(find_most_frequent("Hello,Hello, my dear!"))  # ['hello']
    print(find_most_frequent("to understand recursion you need first to understand recursion..."))  # ['recursion', 'to', 'understand']
    print(find_most_frequent("Mom! Mom! Are you sleeping?!!!"))  # ['mom']
    print("-------")


if __name__ == "__main__":
    main()
