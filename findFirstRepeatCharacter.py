def findFirstRepeatCharacter(string):
    dictionary = {}
    for character in string:
        if character in dictionary:
            return 'The first repeating character is "{}"'.format(character)
            break
        elif character == ' ':
            print('...Skipping empty space.')
            continue
        elif character == '\n':
            print('...Skipping linebreak.')
            continue
        else:
            lowercase_character = set(key.lower() for key in dictionary)
            dictionary[character] = character
            print('"{}" is not a repeat character.'.format(character))
            if character.lower() in lowercase_character:
                print('...FYI, capital and lowercase letters are considered unique characters around here.')
            continue
    return('No repeat characters found!')