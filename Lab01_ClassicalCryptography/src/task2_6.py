import string
import collections

ALPHABET = string.ascii_uppercase

# Tần suất chữ cái tiếng Anh (%)
ENGLISH_FREQ = {
    'A':8.167,'B':1.492,'C':2.782,'D':4.253,'E':12.702,'F':2.228,
    'G':2.015,'H':6.094,'I':6.966,'J':0.153,'K':0.772,'L':4.025,
    'M':2.406,'N':6.749,'O':7.507,'P':1.929,'Q':0.095,'R':5.987,
    'S':6.327,'T':9.056,'U':2.758,'V':0.978,'W':2.360,'X':0.150,
    'Y':1.974,'Z':0.074
}

def normalize(text):
    return ''.join(c for c in text.upper() if c.isalpha())

def index_of_coincidence(text):
    N = len(text)
    freq = collections.Counter(text)
    numerator = sum(v*(v-1) for v in freq.values())
    denominator = N*(N-1)
    return numerator/denominator if denominator != 0 else 0

def guess_key_lengths(ciphertext, max_len=20):
    text = normalize(ciphertext)
    results = []
    for key_len in range(1, max_len+1):
        columns = [text[i::key_len] for i in range(key_len)]
        ic_values = [index_of_coincidence(c) for c in columns]
        avg_ic = sum(ic_values)/len(ic_values)
        results.append((key_len, avg_ic, ic_values))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:6]

def chi_square(column):
    N = len(column)
    freq = collections.Counter(column)
    best_shift = 0
    best_score = float('inf')
    for shift in range(26):
        score = 0
        for i in range(26):
            letter = ALPHABET[i]
            shifted_letter = ALPHABET[(i+shift)%26]
            observed = freq.get(shifted_letter,0)
            expected = ENGLISH_FREQ[letter]*N/100
            score += (observed - expected)**2 / (expected+0.0001)
        if score < best_score:
            best_score = score
            best_shift = shift
    return best_shift

def find_key(ciphertext, key_len):
    text = normalize(ciphertext)
    key = ""
    for i in range(key_len):
        column = text[i::key_len]
        shift = chi_square(column)
        key += ALPHABET[shift]
        print(f"Column {i}: shift={shift}, key char={ALPHABET[shift]}")
    return key

def vigenere_decrypt(ciphertext, key):
    text = normalize(ciphertext)
    key = key.upper()
    plaintext = ""
    for i in range(len(text)):
        c = ALPHABET.index(text[i])
        k = ALPHABET.index(key[i % len(key)])
        p = (c - k) % 26
        plaintext += ALPHABET[p]
    return plaintext

def score_plaintext(plaintext):
    freq = collections.Counter(plaintext)
    N = len(plaintext)
    score = 0
    for letter in ALPHABET:
        observed = freq.get(letter,0)
        expected = ENGLISH_FREQ[letter]*N/100
        score += (observed - expected)**2 / (expected+0.0001)
    return score

def break_vigenere(ciphertext):
    print("\nGuessing key length...\n")
    candidates = guess_key_lengths(ciphertext)
    print("Top key length candidates:")
    for length, avg_ic, ic_values in candidates:
        print(f"Length {length}  Avg IC={avg_ic:.4f}  Column ICs: {[f'{v:.4f}' for v in ic_values]}")

    print("\nTrying candidate keys...\n")
    best_score = float('inf')
    best_plaintext = ""
    best_key = ""
    best_length = 0

    for length, _, _ in candidates:
        print(f"\n--- Trying key length {length} ---")
        key = find_key(ciphertext, length)
        plaintext = vigenere_decrypt(ciphertext,key)
        score = score_plaintext(plaintext)
        print(f"Key guess: {key}  Score: {score:.2f}\nPreview plaintext:\n{plaintext[:200]}\n")

        if score < best_score:
            best_score = score
            best_plaintext = plaintext
            best_key = key
            best_length = length

    print("\n================ BEST RESULT ================")
    print("Key length:", best_length)
    print("Key:", best_key)
    print("Score:", best_score)
    print("Plaintext:\n", best_plaintext)

if __name__ == "__main__":
    choice = input("Nhập 1 để nhập ciphertext từ bàn phím, 2 để đọc từ file: ")
    if choice == "1":
        ciphertext = input("Nhập ciphertext: ")
    elif choice == "2":
        filename = "../data/task2_6_cipher.txt"
        try:
            with open(filename,"r",encoding="utf-8") as f:
                ciphertext = f.read()
        except:
            print("Cannot find ciphertext file:",filename)
            exit()
    else:
        print("Lựa chọn không hợp lệ")
        exit()

    break_vigenere(ciphertext)