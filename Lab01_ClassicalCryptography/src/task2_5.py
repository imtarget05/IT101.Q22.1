import string


def generate_matrix(key):

    key = key.upper().replace(" ", "")
    key = key.replace("J", "I")

    seen = set()
    matrix = []

    for char in key:
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    for char in string.ascii_uppercase:
        if char == 'J':
            continue
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    matrix = [matrix[i:i+5] for i in range(0,25,5)]

    return matrix


def find_position(matrix, letter):

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j


def preprocess(text):

    text = text.upper().replace(" ", "")
    text = text.replace("J","I")

    pairs = []
    i = 0

    while i < len(text):

        a = text[i]

        if i+1 < len(text):
            b = text[i+1]

            if a == b:
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + "X")
            i += 1

    return pairs


def encrypt_pair(matrix, a, b):

    r1,c1 = find_position(matrix,a)
    r2,c2 = find_position(matrix,b)

    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]

    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]

    else:
        return matrix[r1][c2] + matrix[r2][c1]


def decrypt_pair(matrix, a, b):

    r1,c1 = find_position(matrix,a)
    r2,c2 = find_position(matrix,b)

    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

    else:
        return matrix[r1][c2] + matrix[r2][c1]


def encrypt(text,key):

    matrix = generate_matrix(key)

    pairs = preprocess(text)

    cipher = ""

    for p in pairs:
        cipher += encrypt_pair(matrix,p[0],p[1])

    return cipher


def decrypt(cipher,key):

    matrix = generate_matrix(key)

    cipher = cipher.upper()

    plaintext = ""

    for i in range(0,len(cipher),2):

        plaintext += decrypt_pair(matrix,cipher[i],cipher[i+1])

    return plaintext


def print_matrix(matrix):

    print("Playfair Matrix:\n")

    for row in matrix:
        print(" ".join(row))


if __name__ == "__main__":

    key = "HARRY POTTER"

    plaintext = "HELLO WORLD"

    matrix = generate_matrix(key)

    print_matrix(matrix)

    cipher = encrypt(plaintext,key)

    print("\nPlaintext:",plaintext)
    print("Ciphertext:",cipher)

    decrypted = decrypt(cipher,key)

    print("\nDecrypted:",decrypted)