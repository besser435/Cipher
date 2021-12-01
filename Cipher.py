
version = "v1.0"
import string
import random
"""
NOTE
"Encryption is poggers" -Alan Turing, probably


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
rand_char_count = len(chars)


def decode():
    to_decode = input("What is the message you would like to decode? ")
    decode_key = input("Enter the key: ")








    #print("Decoded message: " + decoded_msg)



def encode():
    random_key = []     
    encoded_msg = ""    # the final message
    msg_in = input("What is the message you would like to encode? ")    # what to encode


    for i in range(rand_char_count):     
        char_choice = random.sample(chars, 1)
        random_key.append(char_choice)


    list_t_str = "".join([str(elem) for elem in random_key])
    #list_t_str = str(random_key)    # list to string for the thing below

    
    for letter in msg_in:
        if letter.lower() in chars:
            encoded_msg += list_t_str[chars.find(letter.lower())]   
        else:
            encoded_msg += letter


    print("Encoded message: " + encoded_msg)
    print()
    #print("Your key is: ", *encode_key, sep = "")




action = input("Would you like to encode or decode? e/d ")

if action == "e":
    encode()
elif action == "d":
    decode()
else:
    print("Invalid input")


