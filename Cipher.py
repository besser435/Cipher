
version = "v1.0"


import string
import random


"""
NOTE
This is a very simple method I came up with, but I'm sure its already been discovered and has a proper name


Very bad explanaion considering the message is part of the key lol
Generate and assign a random character to a letter in a message
Key is the alphabet in order, but with random letters
Decoder takes key, see what letter/number/symbol is assigned to the alphabet’s letter, and then decodes the message

Message: abcd
key: a = g, b = 1, c = z, d = & 
Encoded message: g1z&

Key: g1z&
G is in the a spot, 1 is in the b spot, z is in the c spot, & is in the d spot
So decoded it is: abcd


This could probably be cracked in the span of about 10 seconds.
Once you know how it works, all the data is there to decode it.
"""


#string.printable 
#chars = string.printable    # possible key characters
chars = string.ascii_letters


# storage
alphabet = string.ascii_lowercase #string.ascii_lowercase
random_key = ""     # final key
encoded_msg = ""    # message to decode 
decoded_msg = ""

rand_char_count = len(alphabet)
# not done
def decode():
    global encoded_msg
    decode_in = input("What is the message you would like to decode? ")
    decode_key = input("Enter the key: ")


def encode():
    global encoded_msg

    for i in range(rand_char_count):     
        char_choice = random.sample(chars, 1)
        random_key = char_choice
 

    encode_in = input("What is the message you would like to encode? ")


    for letter in encode_in:
        if letter.lower() in alphabet:
            encoded_msg += random_key[alphabet.find(letter.lower())]
        else: encoded_msg += letter

    print("Encoded message: " + encoded_msg)
    print("Your key is: ", *random_key, sep = "")


code_type = input("Would you like to encode or decode? e/d ")

if code_type == "e":
    encode()
elif code_type == "d":
    decode()
else:
    print("Invalid input")


