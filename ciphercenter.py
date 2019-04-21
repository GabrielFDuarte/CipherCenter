# pip install pyfiglet
import pyfiglet
import sys
from ciphers import reverse, caesar

ascii_banner = pyfiglet.figlet_format("CipherCenter")
print("\n")
print(ascii_banner)
print("Created by Gabriel Duarte\n")

print("\nWelcome to CipherCenter. Here you can choose a cipher to encode or decode.\n")

while True:
    opt = input("""Please choose an option:
                1) Encode
                2) Decode 
                3) Exit \n""")

    # Encode
    if opt == '1':
        encOpt = input("""\nPlease choose a cipher to encode:
                1) Reverse Cipher
                2) Caesar Cipher 
                3) ...
                x-1) All 
                x) Exit \n""")
                
        # Reverse Cipher
        if encOpt == '1':
            print("\nReverse Cipher\n")
            revmsg = input("Enter the text to encode: ")
            reverse.reverseEncDec(revmsg)

        # Caesar Cipher
        elif encOpt == '2':
            print("\nCaesar Cipher\n")
            msg = input("Enter the text to encode: ")

            shift = 0
            while True:
                keyStr = input("Enter the key (1-26): ")

                if (keyStr == ""):
                    print("Please enter a valid key...\n")
                else:
                    try:
                        shift = int(keyStr)
                        if (shift >= 1 and shift <= 26):
                            caesar.caesarEncDec(msg, shift, 'encode')
                            break
                        else:
                            print("Please enter a valid key...\n")
                    except ValueError:
                        print("Please enter a valid key...\n")
                    
        # Exit Encode
        elif encOpt == 'x':
            print("Exiting...")
            break

    # Decode
    elif opt == '2':
        decOpt = input("""\nPlease choose a cipher to decode:
                1) Reverse Cipher
                2) Caesar Cipher + Key
                3) Caesar Cipher - All
                4) ... 
                x-1) All 
                x) Exit \n""")
                
        # Reverse Cipher
        if decOpt == '1':
            print("\nReverse Cipher\n")
            revmsg = input("Enter the text to decode: ")
            reverse.reverseEncDec(revmsg)

        # Caesar Cipher using a key
        elif decOpt == '2':
            print("\nCaesar Cipher using Key\n")
            msg = input("Enter the text to decode: ")

            shift = 0
            while True:
                keyStr = input("Enter the key (1-26): ")

                if (keyStr == ""):
                    print("Please enter a valid key...\n")
                else:
                    try:
                        shift = int(keyStr)
                        if (shift >= 1 and shift <= 26):
                            caesar.caesarEncDec(msg, shift, 'decode')
                            break
                        else:
                            print("Please enter a valid key...\n")
                    except ValueError:
                        print("Please enter a valid key...\n")

        # Caesar Cipher using brute force
        elif decOpt == '3':
            print("\nCaesar Cipher - All options\n")
            msg = input("Enter the text to decode: ")
            caesar.bruteforce(msg)
        

        # Exit Decode
        elif decOpt == 'x':
            print("Exiting...")
            

    # Exit
    elif opt == '3':
        print("Exiting...")
        break

    # Wrong option
    elif ((opt != '1') or (opt != '2')):
        print("Wrong option!")
