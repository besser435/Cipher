from json import encoder
import string


################__________________________DONT TOUCH A DAMN THING. IT ACTUALLY WORKS NOW__________________________################

letters = string.ascii_letters
key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'


def encode():
    global encr
    global key
    msg = input("Enter plaintext: ")
    enc = dict(zip(letters, key))
    encr = "".join([enc.get(ch, ch) for ch in msg])

    print(encr)
#encode()



def decode():
    global decr
    msg = input("Enter messge")
    dec = dict(zip(key, letters))
    decr = "".join([dec.get(ch, ch) for ch in msg])

    print(decr)
decode()
