# caesar.py

import string
import os

ALPH = string.ascii_uppercase


def normalize(s, keep_space=False):
    s = s.upper()
    if keep_space:
        return ''.join(ch for ch in s if ch.isalpha() or ch == ' ')
    return ''.join(ch for ch in s if ch.isalpha())


def shift(ch, k):
    return chr((ord(ch) - 65 + k) % 26 + 65)


def encrypt(plaintext, k):
    p = normalize(plaintext, keep_space=True)
    return ''.join(ch if ch == ' ' else shift(ch, k) for ch in p)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


# simple English scoring
COMMON = ["THE", "AND", "TO", "OF", "IN", "IS", "THAT", "IT", "FOR", "ON"]


def score_english(text):
    t = text.upper()
    return sum(t.count(w) * len(w) for w in COMMON)


def brute_force(ciphertext):
    results = []
    for k in range(26):
        pt = decrypt(ciphertext, k)
        results.append((k, score_english(pt), pt))
    return sorted(results, key=lambda x: -x[1])


def read_cipher_file():
    base = os.path.dirname(__file__)
    path = os.path.join(base, "data", "task2_1_cipher.txt")

    with open(path) as f:
        return f.read()


def main():
    while True:
        print("\n=== Caesar Cipher Tool ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute force (file data/task2_1_cipher.txt)")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Enter plaintext: ")
            key = int(input("Enter key: "))
            print("\nCiphertext:")
            print(encrypt(text, key))

        elif choice == "2":
            text = input("Enter ciphertext: ")
            key = int(input("Enter key: "))
            print("\nPlaintext:")
            print(decrypt(text, key))

        elif choice == "3":
            cipher = read_cipher_file()
            results = brute_force(cipher)

            print("\nTop candidate decryptions:\n")
            for k, sc, pt in results[:5]:
                print(f"key={k:2d} score={sc:3d}")
                print(pt[:300])
                print()

        elif choice == "4":
            break


if __name__ == "__main__":
    main()