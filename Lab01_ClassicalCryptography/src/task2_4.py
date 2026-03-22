import string

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

    idx = 0
    table = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(used[idx])
            idx += 1
        table.append(row)

    return table


def findPos(tb, ch):
    for i in range(5):
        for j in range(5):
            if tb[i][j] == ch:
                return i, j
    return -1, -1


def splitText(s):
    s = s.upper().replace("J", "I")
    s = ''.join(ch for ch in s if ch.isalpha())
    res = []
    i = 0
    while i < len(s):
        a = s[i]
        if i + 1 < len(s):
            b = s[i + 1]
            if a == b:
                res.append(a + "X")
                i += 1
            else:
                res.append(a + b)
                i += 2
        else:
            res.append(a + "X")
            i += 1

    return res


def encPair(tb, a, b):
    r1, c1 = findPos(tb, a)
    r2, c2 = findPos(tb, b)
    if r1 == r2:
        return tb[r1][(c1 + 1) % 5] + tb[r2][(c2 + 1) % 5]

    if c1 == c2:
        return tb[(r1 + 1) % 5][c1] + tb[(r2 + 1) % 5][c2]

    return tb[r1][c2] + tb[r2][c1]


def decPair(tb, a, b):
    r1, c1 = findPos(tb, a)
    r2, c2 = findPos(tb, b)

    if r1 == r2:
        return tb[r1][(c1 - 1) % 5] + tb[r2][(c2 - 1) % 5]

    if c1 == c2:
        return tb[(r1 - 1) % 5][c1] + tb[(r2 - 1) % 5][c2]

    return tb[r1][c2] + tb[r2][c1]


def encrypt(txt, key):
    tb = makeTable(key)
    pairs = splitText(txt)
    out = ""
    for p in pairs:
        out += encPair(tb, p[0], p[1])
    return out


def decrypt(txt, key):
    tb = makeTable(key)
    txt = ''.join(ch for ch in txt.upper() if ch.isalpha())
    txt = txt.replace("J", "I")
    out = ""
    i = 0
    while i < len(txt) - 1:
        out += decPair(tb, txt[i], txt[i + 1])
        i += 2
    return out


def showTable(tb):
    print("\n===== MA TRẬN PLAYFAIR 5x5 =====")
    for r in tb:
        print(" ".join(r))
    print("================================\n")

if __name__ == "__main__":
    key = input("Nhập key: ")
    tb = makeTable(key)
    showTable(tb)

    while True:
        print("1. Encrypt (Mã hóa)")
        print("2. Decrypt (Giải mã)")
        print("3. Exit")
        ch = input("Chọn: ").strip()

        if ch == '1':
            t = input("Nhập plaintext: ")
            result = encrypt(t, key)
            print(f"=> Ciphertext: {result}\n")

        elif ch == '2':
            t = input("Nhập ciphertext: ")
            result = decrypt(t, key)
            print(f"=> Plaintext: {result}\n")

        elif ch == '3':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!\n")