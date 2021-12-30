def notes():
    """
    "Encryption is poggers" -Alan Turing, probably 
     I'm hesitant to call it encryption, as it is really bad for countless reasons.`

    Very bad explanaion.
    Randomly generates a key. Each letter in the plaintext is replaced 
    with one letter in the key. It does this for the entire alphabet.
    A would be the first char in the key, B would be the second char in the key,
    ect.

    LAYER1
    Example:
    Plaintext message: abcd
    key: a = g, b = 1, c = z, d = & 
    Encoded message: g1z&
    Key: g1z&
    G is in the A spot, 1 is in the B spot, z is in the C spot, & is in the D spot
    So decoded it is: abcd

    LAYER2
    WIP
    Make it mara
    Known issues:
    Encoding a message longer than the key will break many things like 
    decoding

    """
version = "v1.1"    # code cleanup and UI consistancy is being worked on


import random
import string
import time
import os   

from colorama import init                   # pip install colorama
init()
from colorama import Fore, Style
#init(autoreset=True)   # doesnt work for some reason. its annoying adding the reset flags to everthing


def main():
    def cc():   # long command alias
        os.system("cls" if os.name == "nt" else "clear")

    def ask():  # long command alias
        input("Press enter to continue ")
        cc()
        menu()

    def plain_text_setup():
        global plain_in_char_count
        global plain_in

        plain_in = input("Input your message to encode: ")
        plain_in_char_count = len(plain_in)
    

    def key_gen():
        global shuffled_chars
        global random_chars
        global key_out

        # all the characters that can make up the key
        all_chars = list(string.ascii_letters + string.digits + string.punctuation)  # .printable = problems. thats why this war crime soup is being used

        # same thing as above but randomized
        random.shuffle(all_chars)
        shuffled_chars = "".join(all_chars)


        key_out = shuffled_chars
        def no():   # to collapse
            """
            Ideas:
            maybe the encoder could prefix the key with a number.
            That number would indicate how far in the key is
            just delete the x amount of digits to get to the right spot

            Maybe generate random length caracter chunks, and randomly assign a chunk to a letter
            Combine the two
            This is awful
            Do the above ideas actually improve security? Probably not.

            add error checking to remove spaces at the beginning of things. this is for reasons
            """
 

    def encode_msg(key_out):                        # ENCODE
        global alphabet
        alphabet = string.ascii_letters + string.digits + string.punctuation #+ " " does this add cypertext so spaces can be decrypted?
        
        encode = dict(zip(alphabet, key_out))
        cyphertext = "".join([encode.get(ch, ch) for ch in plain_in])


        print("Your encoded message is:", end="") 
        print(Fore.LIGHTCYAN_EX + cyphertext)
        print(Fore.RESET, end="")
        print()
        print("Your key is:", end="") 
        print(Fore.LIGHTCYAN_EX, *key_out, sep="")
        print(Fore.RESET, end="")
        print()
        ask()

        
    def decode_msg():                               # DECODE
        alphabet = string.ascii_letters + string.digits + string.punctuation #+ " " does this add cypertext so spaces can be decrypted?
        cyphertex_decode_key = input("Input your key: ")
        cyphertex_decode = input("Input your message to decode: ")

        decode = dict(zip(cyphertex_decode_key, alphabet))
        plain_out = "".join([decode.get(ch, ch) for ch in cyphertex_decode])


        print("Your decoded message is: " + Fore.LIGHTCYAN_EX + plain_out + Fore.RESET)
        print()
        ask()
        

    cc()    # clears the text in the IDE on first run
    def menu():
        print("Besser's redneck encryption. 100% secure, I would never lie.")
        print(version)
        
        ask_type = input("Would you like to encode or decode a message? e/d ")
        if ask_type == "e":
            cc()
            plain_text_setup()
            key_gen()
            encode_msg(key_out)
            
        elif ask_type == "d":
            cc()
            decode_msg()

        else:
            cc()
            print("Invalid input")
            menu()
    menu()
main()
