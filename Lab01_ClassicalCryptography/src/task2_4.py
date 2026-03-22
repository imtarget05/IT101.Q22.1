import string
import os

def makeTable(k):
    k = k.upper().replace(" ", "").replace("J", "I")
    used = []
    for ch in k:
        if ch not in used:
            used.append(ch)
    for ch in string.ascii_uppercase:
        if ch == 'J':
            continue
        if ch not in used:
            used.append(ch)
    return [used[i*5:(i+1)*5] for i in range(5)]


def findPos(tb, ch):
    for i in range(5):
        for j in range(5):
            if tb[i][j] == ch:
                return i, j
    return -1, -1


def splitText(s):
    s = ''.join(ch for ch in s.upper().replace("J", "I") if ch.isalpha())
    res = []
    i = 0
    while i < len(s):
        a = s[i]
        if i + 1 < len(s) and s[i+1] != a:
            res.append(a + s[i+1])
            i += 2
        else:
            res.append(a + "X")
            i += 1
    return res


def encPair(tb, a, b):
    r1, c1 = findPos(tb, a)
    r2, c2 = findPos(tb, b)
    if r1 == r2:
        return tb[r1][(c1+1)%5] + tb[r2][(c2+1)%5]
    if c1 == c2:
        return tb[(r1+1)%5][c1] + tb[(r2+1)%5][c2]
    return tb[r1][c2] + tb[r2][c1]


def decPair(tb, a, b):
    r1, c1 = findPos(tb, a)
    r2, c2 = findPos(tb, b)
    if r1 == r2:
        return tb[r1][(c1-1)%5] + tb[r2][(c2-1)%5]
    if c1 == c2:
        return tb[(r1-1)%5][c1] + tb[(r2-1)%5][c2]
    return tb[r1][c2] + tb[r2][c1]


def encrypt(txt, key):
    tb = makeTable(key)
    return ''.join(encPair(tb, p[0], p[1]) for p in splitText(txt))


def decrypt(txt, key):
    tb = makeTable(key)
    txt = ''.join(ch for ch in txt.upper() if ch.isalpha()).replace("J", "I")
    return ''.join(decPair(tb, txt[i], txt[i+1]) for i in range(0, len(txt)-1, 2))


def readFromFile():
    filepath = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "task2_4_cipher.txt")
    )
    if not os.path.exists(filepath):
        print(f"Không tìm thấy file: {filepath}")
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"Đã đọc file: {filepath}")
    return content


def showTable(tb):
    print("\n===== MA TRẬN PLAYFAIR 5x5 =====")
    for row in tb:
        print(" ".join(row))
    print("================================\n")


if __name__ == "__main__":
    key = input("Nhập key: ")
    showTable(makeTable(key))

    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Decrypt từ file task2_4_cipher.txt")
        print("4. Exit")
        ch = input("Chọn: ").strip()

        if ch == '1':
            t = input("Nhập plaintext: ")
            print(f"=> Ciphertext: {encrypt(t, key)}\n")

        elif ch == '2':
            t = input("Nhập ciphertext: ")
            print(f"=> Plaintext: {decrypt(t, key)}\n")

        elif ch == '3':
            content = readFromFile()
            if content:
                print("\n--- Nội dung file ---")
                print(content)
                print("---------------------\n")
                print(f"=> Plaintext: {decrypt(content, key)}\n")

        elif ch == '4':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!\n")