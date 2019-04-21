def caesarEncDec(msg, shift, type):
    result = ''
    i = 0
    while i < len(msg):
        charactere = msg[i]
        if charactere.isalpha():
            nmb = ord(charactere)
            if (type == 'encode'):
                nmb += shift
            elif (type == 'decode'):
                nmb -= shift

            if charactere.isupper():
                if nmb > ord('Z'):
                    nmb -= 26
                elif nmb < ord('A'):
                    nmb += 26
            elif charactere.islower():
                if nmb > ord('z'):
                    nmb -= 26
                elif nmb < ord('a'):
                    nmb += 26

            result += chr(nmb)

        else:
            result += charactere

        i += 1

    print("\nResult:\n", result, "\n")
    
    
def bruteforce(msg):
    print("\nResults:\n")

    for x in range(1,27):
        result = ''
        i = 0
        while i < len(msg):
            charactere = msg[i]
            if charactere.isalpha():
                nmb = ord(charactere)
                nmb -= x

                if charactere.isupper():
                    if nmb > ord('Z'):
                        nmb -= 26
                    elif nmb < ord('A'):
                        nmb += 26
                elif charactere.islower():
                    if nmb > ord('z'):
                        nmb -= 26
                    elif nmb < ord('a'):
                        nmb += 26

                result += chr(nmb)

            else:
                result += charactere

            i += 1

        print("[",x,"] =", result)

    print("\n")