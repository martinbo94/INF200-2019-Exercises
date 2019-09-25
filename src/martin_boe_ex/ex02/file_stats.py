
def char_counts(textfilename):
    """This function imports a file using UTF--8 and reads the unique number
     of characters into a string. It then counts how often each character code
      occurs in the string and returns the result as a list of occupancies
      for the character code"""

    list_with_characters = [0]*256
    with open(textfilename, "r", encoding="UTF--8") as f:
        for char in f.read():
            list_with_characters[ord(char)] += 1
    return list_with_characters


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
