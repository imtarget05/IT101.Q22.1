# auto_mono.py
import re
import random
import os

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# -------------------------
# Normalize text
# -------------------------
def normalize(text, keep_space=False):
    text = text.upper()
    if keep_space:
        return re.sub('[^A-Z ]', '', text)
    return re.sub('[^A-Z]', '', text)

# -------------------------
# Apply substitution key
# -------------------------
def apply_key(ciphertext, key_map):
    s = normalize(ciphertext, keep_space=True)
    result = []

    for ch in s:
        if ch.isalpha():
            result.append(key_map[ch])
        else:
            result.append(ch)

    return ''.join(result)

# -------------------------
# Generate random key
# -------------------------
def random_key():
    letters = list(ALPH)
    random.shuffle(letters)
    return {ALPH[i]: letters[i] for i in range(26)}

# -------------------------
# Score plaintext
# -------------------------
def score_text(text, wordset):
    words = text.split()
    good = sum(1 for w in words if w.lower() in wordset)
    return good

# -------------------------
# Hill-climbing attack
# -------------------------
def hill_climb(ciphertext, wordset, restarts=200, iter_per_restart=2000):

    best = ("", -1, None)

    for r in range(restarts):

        key = random_key()
        cur_plain = apply_key(ciphertext, key)
        cur_score = score_text(cur_plain, wordset)

        for it in range(iter_per_restart):

            a, b = random.sample(list(ALPH), 2)

            new_map = key.copy()

            # swap mapping
            va, vb = new_map[a], new_map[b]
            new_map[a], new_map[b] = vb, va

            pt = apply_key(ciphertext, new_map)
            sc = score_text(pt, wordset)

            if sc > cur_score:
                key = new_map
                cur_score = sc

        if cur_score > best[1]:

            best = (apply_key(ciphertext, key), cur_score, key)

            print("\n[+] New best score:", cur_score)
            print(best[0][:200])

    return best


# -------------------------
# Load word list
# -------------------------
def load_words(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        words = {w.strip().lower() for w in f}

    return words


# -------------------------
# MAIN
# -------------------------
def main():

    base_dir = os.path.dirname(__file__)

    cipher_file = os.path.join(base_dir, "../data/task2_2_cipher.txt")
    word_file = os.path.join(base_dir, "../data/words.txt")

    if not os.path.exists(cipher_file):
        print("Ciphertext file not found:", cipher_file)
        return

    if not os.path.exists(word_file):
        print("Word list file not found:", word_file)
        return

    with open(cipher_file, "r", encoding="utf-8") as f:
        ciphertext = f.read()

    wordset = load_words(word_file)

    print("Ciphertext loaded.")
    print("Dictionary size:", len(wordset))
    print("Starting hill-climb attack...\n")

    plaintext, score, key = hill_climb(ciphertext, wordset)

    print("\n==========================")
    print("FINAL RESULT")
    print("==========================")

    print("\nScore:", score)
    print("\nKey mapping:")

    for k in sorted(key):
        print(k, "->", key[k])

    print("\nPlaintext:\n")
    print(plaintext)


if __name__ == "__main__":
    main()