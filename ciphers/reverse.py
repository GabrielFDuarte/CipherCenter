# Encrypts a text by printing it in reverse order
def reverseEncDec(revmsg):
    result = ''
    i = len(revmsg) - 1
    while i >= 0:
        result += revmsg[i]
        i = i - 1

    print("\nResult:\n", result, "\n")