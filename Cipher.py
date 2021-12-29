def notes():
    """
    "Encryption is poggers" -Alan Turing, probably 

    Very bad explanaion because the key and encoded message are the same
    Generate and assign a random character to a letter in a message
    The key is the alphabet in order, but with random letters
    Decoder takes key, see what letter/number/symbol is assigned to the alphabet’s letter, and then decodes the message
    If I'm not mistaken, its a type of a transposition cipher.

    I'm hesitant to call it encrytion.


    Message: abcd
    key: a = g, b = 1, c = z, d = & 
    Encoded message: g1z&

    Key: g1z&
    G is in the A spot, 1 is in the B spot, z is in the C spot, & is in the D spot
    So decoded it is: abcd


    This could probably be cracked in the span of about 0.00000000001 seconds.

    """
version = "v1.0 beta (functional, but buggy)"
debug = 1


import random
import string
import time
import os   

def main():
    def cc():   # shortens long command to just cc()
        os.system("cls" if os.name == "nt" else "clear")


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
        all_chars = list(string.ascii_letters + string.digits + string.punctuation)  # string.printable create problems. thats why this war crime soup is being used


        # same thing as above but randomized
        random.shuffle(all_chars)
        shuffled_chars = "".join(all_chars)

        key_out = shuffled_chars
        
        def no():
            """
            Ideas:
            maybe the encoder could prefix the key with a number.
            That number would indicate how far in the key is

            Maybe generate random length caracter chunks, and randomly assign a chunk to a letter

            Combine the two
            This is awful
            Do the above ideas actually improve security? Probably not.
            """

    
    def encode_msg(key_out):
        global alphabet
        alphabet = string.ascii_letters + string.digits + string.punctuation #+ " " does this add cypertext so spaces can be decrypted?
        
        encode = dict(zip(alphabet, key_out))
        cyphertext = "".join([encode.get(ch, ch) for ch in plain_in])

        
        print("Your key is:", end="") 
        print(*key_out, sep="")
        print("Your encoded message is:" + cyphertext)
        print()
        input("Press enter to continue")
        cc()
        menu()

        
    def decode_msg():
        alphabet = string.ascii_letters + string.digits + string.punctuation #+ " " does this add cypertext so spaces can be decrypted?
        cyphertex_decode_key = input("Input your key: ")
        cyphertex_decode = input("Input your message to decode: ")

        decode = dict(zip(alphabet, cyphertex_decode_key))
        plain_out = "".join([decode.get(ch, ch) for ch in cyphertex_decode])
        print(plain_out)
        

    """    def print_debug():    # in a bad state right now. Because this project is pretty simple, this isnt really needed.
        global debug
        if debug:
            print("DEBUG: ")
            print(version)
            print("Plain text input: " + plain_in)
            print("Input char count: " + str(plain_in_char_count))
            print("All chars shuffled: " + shuffled_chars)
            print()
    """

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
            main()

            
    menu()
    
main()
