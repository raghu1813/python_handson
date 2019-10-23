import re
from ngramscore import ngram_score
from pycipher import Caesar

fitness = ngram_score('english_quadgrams.txt')


def break_caesar(ctext):
    # make sure ciphertext has all spacing/punc removed and is uppercase
    ctext = re.sub('[^A-Z]', '', ctext.upper())
    # try all possible keys, return the one with the highest fitness
    scores = []
    for i in range(26):
        scores.append((fitness.score(Caesar(i).decipher(ctext)), i))
    return max(scores)

def main():
    # example ciphertext
    ctext=input("enter cipher text")
    max_key = break_caesar(ctext)

    print('best candidate with key (a,b) = ' + str(max_key[1]) + ':')
    print(Caesar(max_key[1]).decipher(ctext))

if __name__ == "__main__":
    main()
