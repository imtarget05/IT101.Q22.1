from Crypto.Cipher import DES

def bytes_to_bin(data):
    return bin(int.from_bytes(data, 'big'))[2:].zfill(len(data) * 8)

def hamming_distance(b1, b2):
    return sum(bit1 != bit2 for bit1, bit2 in zip(b1, b2))

def avalanche_test():
    key = b'87654321'  
    p1 = b'STAYHOME'
    p2 = b'STAYHOMA'

    cipher = DES.new(key, DES.MODE_ECB)

    c1 = cipher.encrypt(p1)
    c2 = cipher.encrypt(p2)

    b1 = bytes_to_bin(c1)
    b2 = bytes_to_bin(c2)

    diff_bits = hamming_distance(b1, b2)
    total_bits = len(b1)

    percentage = (diff_bits / total_bits) * 100

    print("Ciphertext 1:", c1.hex())
    print("Ciphertext 2:", c2.hex())
    print("Binary 1:", b1)
    print("Binary 2:", b2)
    print("Số bit khác nhau:", diff_bits)
    print("Tổng số bit:", total_bits)
    print(f"Tỷ lệ thay đổi: {percentage:.2f}%")

avalanche_test()