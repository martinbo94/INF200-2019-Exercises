def bubble_sort(data):
    """ Bubble sort compares the first and the second number, and if the first number is larger than the second, the
    order will be switched. This is the reason why the last number will always be the largest one, as it gets pushed
    all the way to the back.
    """
    sorted_list = list(data)
    for i in range(0, len(sorted_list) - 1):
        for j in range(0, len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j+1], sorted_list[j]

    return sorted_list


if __name__ == "__main__":
    for data in ((),
                (1,),
                (1, 3, 8, 12),
                (12, 8, 3, 1),
                (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
