def Crack(P, C):
    P = [ord(x) - 65 for x in list(P)]
    C = [ord(x) - 65 for x in list(C)]
    #print(P, C)
    a = (C[0] - C[1]) / (P[0] - P[1])
    b = (P[0] * C[1] - C[0] * P[1]) / (P[0] - P[1])
    key = [a, b]
    key = (int(a), int(b))
    key = [(x + 26) % 26 for x in key]
    return key




def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m



def affine_encrypt(text, key):

    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


def affine_decrypt(cipher, key):

    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])


def main():

    msg=input("enter the message\n").upper()
    key = input("enter the key\n").split(",")
    key=[int(x) for x in list(key)]

    affine_encrypted_text = affine_encrypt(msg, key)

    print('Encrypted Text: {}'.format(affine_encrypted_text))

    print('Decrypted Text: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))

    ci=input("enter cipher to generate key space")


    for i in range(26):
        for j in [1,3,5,7,9,11,15,17,19,21,23,25]:
            key=[j,i]
            x=affine_decrypt(ci,key)
            print(x)

    print("Known plain Text Attack in AffineCipher")
    P = input("Enter PlainText: ").upper()
    C = input("Enter CipherText: ").upper()
    key = Crack(P, C)
    print(key)

if __name__ == '__main__':
    main()
