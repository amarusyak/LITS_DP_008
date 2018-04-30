import ast


def unpack_list(lst):
    """
    Unpacks nested lists
    :param lst: input nested list
    :return: sorted unpacked list
    """
    lst = ast.literal_eval(lst)
    while any(isinstance(el, list) for el in lst):
        for el in lst:
            index = lst.index(el)
            el = lst.pop(index)

            if type(el) is list:
                lst.extend(el)
            elif type(el) is int:
                lst.append(el)
            else:
                raise TypeError(
                    "Incorrect element type - {t}. "
                    "Type should be 'list' or 'int'.".format(
                        t=type(el))
                )

    return sorted(lst)


def is_parenthesis_balanced(string):
    """
    Checks if parenthesis are balanced in the string
    :param string: input string containing parenthesis
    :return: True/False depending on whether parenthesis 
        are balanced or not
    """
    return string.count('(') is string.count(')')


def main():
    nested_list = input("Enter list sequence: ")
    print("Result: " + str(unpack_list(nested_list)))

    print()

    input_str = input("Enter some string containing parenthesis: ")
    print("Parenthesis are balanced!" if is_parenthesis_balanced(input_str)
          else "Parenthesis are NOT balanced :(")


if __name__ == "__main__":
    main()
