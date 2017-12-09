import string
alpha_lower = list(string.ascii_lowercase)

def alphabet_position(letter):
    return alpha_lower.index(letter.lower())


def rotate_character(char, rot):
    new_letter=alphabet_position(char) + rot
    small_letter=char.islower()
    lower_letter=''
    if new_letter>=26:
        lower_letter= string.lowercase[new_letter%26]
    else:
        lower_letter= string.lowercase[new_letter]
    if small_letter:
        return lower_letter
    else:
        return lower_letter.upper()

