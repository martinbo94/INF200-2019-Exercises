def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """Re-wrote the squares_by_comp function to return the squares by loop instead"""
    liste = []
    for number in range(n):
        if number % 3 == 1:
            liste.append(number**2)
    return liste


if __name__ == '__main__':
    if squares_by_comp(10) != squares_by_loop(10):
        print('Error!')
