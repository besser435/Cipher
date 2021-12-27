def notes():
    """
    "Encryption is poggers" -Alan Turing, probably 

    Very bad explanaion because the key and encoded message are the same
    Generate and assign a random character to a letter in a message
    The key is the alphabet in order, but with random letters
    Decoder takes key, see what letter/number/symbol is assigned to the alphabet’s letter, and then decodes the message
    If I'm not mistaken, its a type of a transposition cipher.


    Message: abcd
    key: a = g, b = 1, c = z, d = & 
    Encoded message: g1z&

    Key: g1z&
    G is in the A spot, 1 is in the B spot, z is in the C spot, & is in the D spot
    So decoded it is: abcd


    This could probably be cracked in the span of about 0.00000000001 seconds.

    """
version = "v0.2 (unbunged version of 0.1)"
debug = 0


import random
import string
import os

def main():
    def cc():   # shortens long command to just cc()
        os.system("cls" if os.name == "nt" else "clear")


    def plain_text_setup():
        global plain_in_char_count
        global plain_in

        plain_in = "Hello World"
        plain_in_char_count = len(plain_in)
    

    def key_gen():
        global shuffled_chars
        global random_chars
        global key_out

        # all the characters that can make up the key
        all_chars = list(string.ascii_letters + string.digits + 
        string.punctuation)  # string.printable create problems. thats why this war crime soup is being used

        # same thing as above but randomized
        random.shuffle(all_chars)
        shuffled_chars = "".join(all_chars)


        key_out = all_chars[0:26] 
        """
        Ideas:
        Try getting rid of limit, maybe the encoder could prefix the key with a number.
        That number would indicate how far in the key is

        Maybe generate random length caracter chunks, and randomly assign a chunk to a letter

        Combine the two
        This is awful
        Do the above ideas actually improve security? Probably not.
        """

    
    def encode_msg(key):
        
        cyphertext = "" # final message

        print(key)
        
        
        
        
        print("Your key is: ", end="") 
        print(*key_out, sep="")
        print("Your encoded message is: ")
        print()
        input("Press enter to continue")
        cc()
        menu()


    def decode_msg():
        pass


    def print_debug():    # stuff to print if debug moce is enabled
        global debug
        if debug:
            print()
            print("DEBUG:")
            print(version)
            print("Plain text input: " + plain_in)
            print("Input char count: " + str(plain_in_char_count))
            print("All chars shuffled: " + shuffled_chars)
            print()


    def menu():
        

        print("Besser's redneck encryption. 100% secure, I would never lie.")
        print_debug()
        print(version)

        ask_type = input("Would you like to encode or decode a message? e/d ")
        if ask_type == "e":
            cc()
            plain_text_setup()
            key_gen()
            encode_msg(key_out)

        elif ask_type == "d":
            pass

        else:
            pass


    menu()
main()
