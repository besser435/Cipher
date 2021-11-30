version = "v1.0"

"""
NOTE
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


This could probably be cracked in the span of about 10 seconds
"""

 
def encode():
    encode_in = input("What is the message you would like to encode? ")


def decode():
    decode_in = input("What is the message you would like to decode? ")
    decode_key = input("Enter the key: ")




code_type = input("Would you like to encode or decode? e/d ")

if code_type == "e":
    encode()
elif code_type == "d":
    decode()