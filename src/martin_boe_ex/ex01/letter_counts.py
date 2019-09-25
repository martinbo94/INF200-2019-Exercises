def letter_freq(txt):
    txt = txt.lower()
    empty_dict = {}
    for character in txt:
        empty_dict[character] = txt.count(character)

    return empty_dict


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
