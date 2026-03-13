import random
import re
from collections import Counter

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# -----------------------------
# TEXT NORMALIZATION
# -----------------------------

def normalize(text):
    text = text.upper()
    return re.sub('[^A-Z]', '', text)


# -----------------------------
# APPLY KEY
# -----------------------------

def decrypt(ciphertext, key):

    mapping = dict(zip(ALPHABET, key))

    plaintext = ""

    for c in ciphertext:
        plaintext += mapping.get(c, c)

    return plaintext


# -----------------------------
# ENGLISH SCORING
# -----------------------------

COMMON_WORDS = [
"THE","AND","TO","OF","IN","IS","THAT","IT",
"FOR","ON","WITH","AS","AT","BY"
]

def score_text(text):

    score = 0

    for word in COMMON_WORDS:
        score += text.count(word) * len(word)

    return score


# -----------------------------
# RANDOM KEY
# -----------------------------

def random_key():

    letters = list(ALPHABET)

    random.shuffle(letters)

    return "".join(letters)


# -----------------------------
# MUTATE KEY
# -----------------------------

def swap_key(key):

    a,b = random.sample(range(26),2)

    key_list = list(key)

    key_list[a],key_list[b] = key_list[b],key_list[a]

    return "".join(key_list)


# -----------------------------
# HILL CLIMB
# -----------------------------

def hill_climb(ciphertext, iterations=2000):

    key = random_key()

    best_key = key
    best_score = -1

    for _ in range(iterations):

        candidate = swap_key(key)

        plaintext = decrypt(ciphertext, candidate)

        score = score_text(plaintext)

        if score > best_score:
            best_score = score
            best_key = candidate
            key = candidate

    return best_key, best_score


# -----------------------------
# SOLVER
# -----------------------------

def solve(ciphertext, restarts=200):

    ciphertext = normalize(ciphertext)

    best_key = None
    best_score = -1
    best_plaintext = ""

    for i in range(restarts):

        key,score = hill_climb(ciphertext)

        if score > best_score:

            best_score = score
            best_key = key
            best_plaintext = decrypt(ciphertext,key)

            print("\nBetter result found!")
            print("Score:",score)
            print("Key:",key)
            print("Preview:")
            print(best_plaintext[:300])

    return best_key,best_plaintext


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    import os

    base_dir = os.path.dirname(__file__)

    file_path = os.path.join(base_dir,"../data/task2_2_cipher.txt")

    if not os.path.exists(file_path):

        print("Ciphertext file not found:",file_path)
        exit()

    with open(file_path,"r",encoding="utf-8") as f:
        ciphertext = f.read()

    print("Ciphertext loaded\n")

    key,plaintext = solve(ciphertext)

    print("\n==============================")
    print("FINAL RESULT")
    print("==============================")

    print("Key:",key)

    print("\nPlaintext:\n")

    print(plaintext)