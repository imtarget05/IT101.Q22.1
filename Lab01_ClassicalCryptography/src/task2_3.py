# auto_mono_refined.py
import re
import random
import math
import os

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def normalize(text, keep_space=False):
    text = text.upper()
    if keep_space:
        return re.sub('[^A-Z ]', '', text)
    return re.sub('[^A-Z]', '', text)


def apply_key(ciphertext, key_map):
    s = normalize(ciphertext, keep_space=True)
    return ''.join(key_map.get(c, c) for c in s)


def random_key():
    letters = list(ALPH)
    random.shuffle(letters)
    return {ALPH[i]: letters[i] for i in range(26)}


def swap_key(key):
    a, b = random.sample(ALPH, 2)
    new_key = key.copy()
    new_key[a], new_key[b] = new_key[b], new_key[a]
    return new_key


BIGRAMS = {
    "TH": 2.0, "HE": 2.0, "IN": 1.5, "ER": 1.5,
    "AN": 1.5, "RE": 1.2, "ON": 1.2, "AT": 1.2,
    "EN": 1.2, "ND": 1.2, "TI": 1.1, "ES": 1.1,
    "OR": 1.1, "TE": 1.1, "OF": 1.0, "ED": 1.0
}

def bigram_score(text):
    score = 0
    text = text.replace(" ", "")
    for i in range(len(text) - 1):
        score += BIGRAMS.get(text[i:i+2], 0)
    return score


def dict_score(text, wordset):
    words = text.split()
    return sum(1 for w in words if w.lower() in wordset)


def score_text(text, wordset):
    return dict_score(text, wordset) * 5 + bigram_score(text)


def simulated_annealing(ciphertext, wordset,
                        max_iter=10000,
                        start_temp=5.0,
                        cooling=0.0005):

    key = random_key()
    current_text = apply_key(ciphertext, key)
    current_score = score_text(current_text, wordset)

    best = (current_text, current_score, key)

    T = start_temp

    for i in range(max_iter):

        new_key = swap_key(key)
        new_text = apply_key(ciphertext, new_key)
        new_score = score_text(new_text, wordset)

        delta = new_score - current_score

        # Accept condition
        if delta > 0 or random.random() < math.exp(delta / T):
            key = new_key
            current_score = new_score
            current_text = new_text

        # Update best
        if current_score > best[1]:
            best = (current_text, current_score, key)

        # Cooling
        T *= (1 - cooling)

        if i % 1000 == 0:
            print(f"[Iter {i}] Score = {current_score}")

    return best


def solve(ciphertext, wordset, runs=10):
    best = ("", -1, None)

    for i in range(runs):
        print(f"\n=== Run {i+1} ===")

        res = simulated_annealing(ciphertext, wordset)

        if res[1] > best[1]:
            best = res
            print("\n[+] NEW GLOBAL BEST:", res[1])
            print(res[0][:200])

    return best


def load_words(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return {w.strip().lower() for w in f}


def main():

    base_dir = os.path.dirname(__file__)
    word_file = os.path.join(base_dir, "../data/words.txt")

    if not os.path.exists(word_file):
        print("Word list file not found:", word_file)
        return

    wordset = load_words(word_file)

    print("===== MONOALPHABETIC CIPHER ATTACK =====")
    print("1. Read ciphertext from file")
    print("2. Input ciphertext manually")

    choice = input("Choose option (1 or 2): ").strip()

    if choice == "1":
        cipher_file = os.path.join(base_dir, "../data/task2_2_cipher.txt")

        if not os.path.exists(cipher_file):
            print("Ciphertext file not found:", cipher_file)
            return

        with open(cipher_file, "r", encoding="utf-8") as f:
            ciphertext = f.read()

        print("\n[+] Ciphertext loaded from file.\n")

    elif choice == "2":
        print("\nEnter your ciphertext (end with ENTER):")
        ciphertext = input("> ")

        if not ciphertext.strip():
            print("Empty input. Exiting.")
            return

    else:
        print("Invalid choice.")
        return

    print("\nStarting attack...\n")

    plaintext, score, key = solve(ciphertext, wordset)

    print("\n====================")
    print("FINAL RESULT")
    print("====================")

    print("\nScore:", score)

    print("\nKey mapping:")
    for k in sorted(key):
        print(k, "->", key[k])

    print("\nPlaintext:\n")
    print(plaintext)

if __name__ == "__main__":
    main()