from helpers import alphabet_position, rotate_character


def encrypt(text, key):
    new_string = ""
    index = 0
    for letter in text:
        if letter.isspace():
            new_string += letter
        elif not letter.isalpha():
            new_string += letter 
        else:
            new_string += rotate_character(letter, alphabet_position(key[index]))
            index += 1
        if(index > len(key)-1):
            index = 0
    return new_string


def main():
    print(encrypt("The crow flies at midnight!", "boom"))

if __name__ == "__main__":
    main()
