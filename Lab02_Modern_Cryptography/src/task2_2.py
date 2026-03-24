from Crypto.Cipher import AES

key = b'1234567890123456'
plaintext = b"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_" 

cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(plaintext)

iv = b'\x00' * 16
cipher_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
ct_cbc = cipher_cbc.encrypt(plaintext)

print(f"ECB Hex: {ct_ecb.hex()}")
print(f"CBC Hex: {ct_cbc.hex()}")
