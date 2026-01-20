import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# Encrypt
print("----------------------------------------")
plain_text = input("Enter a message to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("----------------------------------------")
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")
print("----------------------------------------")
print("----------------------------------------")

# Decrypt
cipher_text = input("Enter a message to Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("----------------------------------------")
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
print("----------------------------------------")