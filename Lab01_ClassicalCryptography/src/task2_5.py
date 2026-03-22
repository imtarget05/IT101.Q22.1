import os

def normalize(text):
    return ''.join(ch.upper() for ch in text if ch.isalpha())


def encrypt(plaintext, key):
    plain, k = normalize(plaintext), normalize(key)
    klen = len(k)
    return ''.join(
        chr((ord(ch) - ord('A') + ord(k[i % klen]) - ord('A')) % 26 + ord('A'))
        for i, ch in enumerate(plain)
    )

def decrypt(ciphertext, key):
    k = normalize(key)
    klen = len(k)
    result = []
    idx = 0  

    for ch in ciphertext:
        if ch.isalpha():
            c = ord(ch.upper()) - ord('A')
            ki = ord(k[idx % klen]) - ord('A')
            p = (c - ki + 26) % 26
            result.append(chr(p + ord('A')))
            idx += 1
        else:
            result.append(ch)  

    return ''.join(result)


def keyStream(text, key):
    plain, k = normalize(text), normalize(key)
    return ''.join(k[i % len(k)] for i in range(len(plain)))


def readFromFile():
    filepath = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "task2_5_cipher.txt")
    )
    if not os.path.exists(filepath):
        print(f"Không tìm thấy file: {filepath}")
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"Đã đọc file: {filepath}")
    return content


if __name__ == "__main__":
    key = input("Nhập key: ").strip() 
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Decrypt từ file task2_5_cipher.txt")
        print("4. Exit")
        ch = input("Chọn: ").strip()

        if ch == '1':
            t = input("Nhập plaintext: ")
            result = encrypt(t, key)
            print(f"=> Key stream : {keyStream(t, key)}")
            print(f"=> Plaintext  : {normalize(t)}")
            print(f"=> Ciphertext : {result}\n")

        elif ch == '2':
            t = input("Nhập ciphertext: ")
            result = decrypt(t, key)
            print(f"=> Plaintext  : {result}\n")

        elif ch == '3':
            content = readFromFile()
            if content:
                print("\n--- Nội dung file ---")
                print(content)
                print("---------------------\n")
                result = decrypt(content, key)
                print(f"=> Plaintext  : {result}\n")

        elif ch == '4':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!\n")