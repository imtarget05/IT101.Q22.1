import string

def normalize(text):
    return ''.join(ch.upper() for ch in text if ch.isalpha())


def encrypt(plaintext, key):
    plain = normalize(plaintext)
    key_norm = normalize(key)

    if not key_norm:
        print("Key không hợp lệ!")
        return ""

    cipher = ""
    key_len = len(key_norm)

    for i, ch in enumerate(plain):
        p = ord(ch) - ord('A')
        k = ord(key_norm[i % key_len]) - ord('A')
        c = (p + k) % 26
        cipher += chr(c + ord('A'))

    return cipher


def decrypt(ciphertext, key):
    cipher = normalize(ciphertext)
    key_norm = normalize(key)

    if not key_norm:
        print("Key không hợp lệ!")
        return ""

    plain = ""
    key_len = len(key_norm)

    for i, ch in enumerate(cipher):
        c = ord(ch) - ord('A')
        k = ord(key_norm[i % key_len]) - ord('A')
        p = (c - k + 26) % 26
        plain += chr(p + ord('A'))

    return plain


def showKeyStream(plaintext, key):
    plain = normalize(plaintext)
    key_norm = normalize(key)
    key_len = len(key_norm)
    stream = ''.join(key_norm[i % key_len] for i in range(len(plain)))
    return stream


if __name__ == "__main__":
    key = input("Nhập key: ").strip()

    while True:
        print("\n1. Encrypt (Mã hóa)")
        print("2. Decrypt (Giải mã)")
        print("3. Exit")
        ch = input("Chọn: ").strip()

        if ch == '1':
            t = input("Nhập plaintext: ")
            result = encrypt(t, key)
            print(f"=> Key stream   : {showKeyStream(t, key)}")
            print(f"=> Plaintext    : {normalize(t)}")
            print(f"=> Ciphertext   : {result}\n")

        elif ch == '2':
            t = input("Nhập ciphertext: ")
            result = decrypt(t, key)
            print(f"=> Ciphertext   : {normalize(t)}")
            print(f"=> Plaintext    : {result}\n")
            
        elif ch == '3':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!\n")