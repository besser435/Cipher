from json import encoder
import os
import string


################__________________________DONT TOUCH A DAMN THING. IT ACTUALLY WORKS NOW__________________________################
## THIS SERVES AS WHERE THE VARS GO IN TH FUNCTIONS
## the key remains static for this simple example, but it can be randomized
def main():
    global key


    letters = string.ascii_letters
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'


    def cc():   # shortens long command to just cc()
        os.system("cls" if os.name == "nt" else "clear")


    def encode():
        msg = input("Enter plaintext: ")
        enc = dict(zip(letters, key))
        encr = "".join([enc.get(ch, ch) for ch in msg])

        print(encr)


    def decode():
        msg = input("Enter messge")
        dec = dict(zip(key, letters))
        decr = "".join([dec.get(ch, ch) for ch in msg])

        print(decr)


    def menu():
        ask_type = input("Would you like to encode or decode a message? e/d ")
        if ask_type == "e":
            cc()
            encode()
        elif ask_type == "d":
            cc()
            decode()

        else:
            cc()
            print("Invalid input")
    menu()
main()
    

