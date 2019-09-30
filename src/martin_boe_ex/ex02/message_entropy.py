from math import log2


def letter_freq(txt):
    txt = txt.lower()
    empty_dict = {}
    for character in txt:
        empty_dict[character] = txt.count(character)

    return empty_dict


def entropy(message):
    """ This function calculate the Entropy of a string, using the letter_freq
    function to count the number of occurrences per character"""
    freq = letter_freq(message)
    n = sum(freq.values())

    h = 0

    for n_i in freq.values():
        p_i = n_i/n
        h += -p_i * log2(p_i)

    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
