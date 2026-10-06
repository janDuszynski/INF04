textToEncrypt = input("Wprowadź tekst do zaszyfrowania: ")
encryptionKey = int(input("Wprowadź długość klucza: "))

encrypted = ""

for char in textToEncrypt:
    if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        encrypted += chr((ord(char) - ascii_offset + encryptionKey) % 26 + ascii_offset)
    else:
        encrypted += char

print("Zaszyfrowany tekst:", encrypted)
