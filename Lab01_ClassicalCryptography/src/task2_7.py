import re

def normalize(text):
    text = text.upper()
    return re.sub('[^A-Z]', '', text)

def rail_fence_encrypt(plaintext, rails):

    text = normalize(plaintext)

    fence = ['' for _ in range(rails)]

    rail = 0
    direction = 1

    for char in text:

        fence[rail] += char

        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    ciphertext = ''.join(fence)

    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    text = normalize(ciphertext)
    pattern = []
    rail = 0
    direction = 1
    for _ in range(len(text)):

        pattern.append(rail)

        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    rail_counts = [pattern.count(r) for r in range(rails)]
    rails_data = []
    index = 0

    for count in rail_counts:
        rails_data.append(list(text[index:index+count]))
        index += count

    plaintext = ""
    rail_indices = [0]*rails

    for r in pattern:

        plaintext += rails_data[r][rail_indices[r]]

        rail_indices[r] += 1

    return plaintext


if __name__ == "__main__":

    plaintext = "WE ARE DISCOVERED FLEE AT ONCE"

    rails = 3

    print("Original Plaintext:")
    print(plaintext)

    ciphertext = rail_fence_encrypt(plaintext, rails)

    print("\nEncrypted (Rail Fence):")
    print(ciphertext)

    decrypted = rail_fence_decrypt(ciphertext, rails)

    print("\nDecrypted:")
    print(decrypted)