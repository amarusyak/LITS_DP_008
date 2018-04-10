def unpack_list(lst):
    """
    Unpacks nested lists
    :param lst: input nested list
    :return: sorted unpacked list
    """
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


def main():
    nested_list = input("Enter list sequence: ")
    print "Result: " + str(unpack_list(nested_list))


if __name__== "__main__":
    main()
