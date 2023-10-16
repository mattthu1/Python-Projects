# function #1: ascii_shift
def ascii_shift(word, num):
    if word == "":
        return ""
    shifted = ""
    for char in word:
        shifted += chr(ord(char) + num)
    return shifted

# function #2: shift_right
def shift_right(word):
    if word == "":
        return ""
    shifted = word[-1] + word[:-1]
    return shifted

# function #3: shift_left
def shift_left(word):
    if word == "":
        return ""
    shifted = word[1:] + word[0]
    return shifted

# function #4: flip
def flip(word):
    if word == "":
        return ""
    mid = len(word) // 2
    if len(word) % 2 == 0:
        flipped = word[mid:] + word[:mid]
    else:
        flipped = word[mid+1:] + word[mid] + word[:mid]
    return flipped

# function #5: add_letters
import random
import string

def add_letters(word, num):
    if word == "":
        return ""
    scrambled = ""
    for char in word:
        scrambled += char
        for i in range(num):
            scrambled += random.choice(string.ascii_letters)
    return scrambled


# function #6: delete_characters

def delete_characters(word, num):
    new_word = ""
    for i in range(len(word)):
        if i % (num+1) == 0:
            new_word += word[i]
    return new_word


