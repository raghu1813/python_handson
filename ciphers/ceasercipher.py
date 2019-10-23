
def decrypt(msg,n,k):
    res=""
    for i in range(n):
        tp = msg[i]
        if (tp.isupper()):
            res += chr((ord(tp) - 65 - k) % 26 + 65)
        else:
            res += chr((ord(tp) - 97 - k) % 26 + 97)
    print(res)
    return res




def encrypt(msg,n,k):
    res1=""
    for i in range(n):
        tp=msg[i]
        if(tp.isupper()):
            res1 += chr((ord(tp) -65+ k) % 26 +65)
        else:
            res1 +=chr((ord(tp)-97+k)%26 +97)
    return res1






def Encrypt(K, P):
    cipher = []
    for letter in P:
        cipher.append(chr((ord(letter) - 65 + K) % 26 + 65))
    return "".join(cipher)


def Crack(C, P):
    key = -1
    while key <= 25:
        key += 1
        if C == Encrypt(key, P):
            break
    return key


def main():
    msg = input("enter the message")
    print(msg)

    n = len(msg)
    k = int(input("enter the key to encrypt"))
    cipher = encrypt(msg, n, k)
    print("your message encrypted \n")
    print("encrypted msg is ", cipher)
    dec = decrypt(cipher, n, k)
    print("decrypted msg is ", dec)
    print("----the known plain text attack---")

    cipher = input("Enter Cipher Text: ")
    plain = input("Enter Plain Text: ")
    key = Crack(cipher.upper(),plain.upper())
    print("Key =", key)


if __name__ == "__main__":
    main()






