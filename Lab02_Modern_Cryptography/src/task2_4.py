from Crypto.Cipher import AES

BLOCK_SIZE = 16

def split_blocks(data, size=16):
    return [data[i:i+size] for i in range(0, len(data), size)]

def flip_bit(data, byte_index, bit_index):
    data = bytearray(data)
    data[byte_index] ^= (1 << bit_index)
    return bytes(data)

def analyze_blocks(original, decrypted):
    orig_blocks = split_blocks(original)
    dec_blocks = split_blocks(decrypted)

    corrupted_indices = []

    for i in range(len(orig_blocks)):
        if orig_blocks[i] != dec_blocks[i]:
            corrupted_indices.append(i)

    return corrupted_indices, orig_blocks, dec_blocks

def test_mode(mode_name, mode):
    print(f"\n===== {mode_name} =====")

    key = b'1234567890123456'
    iv = b'1234567890123456'

    plaintext = b'A' * 1000

    pad_len = BLOCK_SIZE - (len(plaintext) % BLOCK_SIZE)
    padded = plaintext + bytes([pad_len] * pad_len)

    if mode_name == "ECB":
        cipher = AES.new(key, mode)
    else:
        cipher = AES.new(key, mode, iv=iv)

    ciphertext = cipher.encrypt(padded)

    byte_index = 25
    bit_index = 0
    corrupted_ct = flip_bit(ciphertext, byte_index, bit_index)

    error_block = byte_index // BLOCK_SIZE

    print(f"Flip tại byte: {byte_index} (thuộc block {error_block})")

    if mode_name == "ECB":
        decipher = AES.new(key, mode)
    else:
        decipher = AES.new(key, mode, iv=iv)

    decrypted = decipher.decrypt(corrupted_ct)

    corrupted_indices, orig_blocks, dec_blocks = analyze_blocks(padded, decrypted)

    total_blocks = len(orig_blocks)
    num_corrupted = len(corrupted_indices)

    print(f"Tổng block: {total_blocks}")
    print(f"Block bị lỗi: {corrupted_indices}")
    print(f"Số block bị lỗi: {num_corrupted}")
    print(f"Tỷ lệ lỗi: {(num_corrupted/total_blocks)*100:.2f}%")

    print("\nChi tiết các block bị lỗi:")
    for i in corrupted_indices:
        print(f"\n--- Block {i} ---")
        print("Original :", orig_blocks[i].hex())
        print("Decrypted:", dec_blocks[i].hex())

def main():
    test_mode("ECB", AES.MODE_ECB)
    test_mode("CBC", AES.MODE_CBC)
    test_mode("CFB", AES.MODE_CFB)
    test_mode("OFB", AES.MODE_OFB)

if __name__ == "__main__":
    main()