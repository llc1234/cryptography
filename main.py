class cryptography:
    def __init__(self):
        self.key = []

    def encrypt(self, string):
        text = string.encode().hex()

        in_key = 0

        li = []
        for pp in range(0, len(text), 2):
            hex_to_int = int(text[pp] + text[pp + 1], 16)
            li.append(hex_to_int + self.key[in_key])

            in_key += 1
            if in_key > len(self.key)-1:
                in_key = 0

        enc = "".join([format(pp, 'x') for pp in li])
        return enc

    def decrypt(self, string):
        text = string

        in_key = 0

        li = []
        for pp in range(0, len(text), 2):
            hex_to_int = int(text[pp] + text[pp + 1], 16)
            li.append(hex_to_int - self.key[in_key])

            in_key += 1
            if in_key > len(self.key)-1:
                in_key = 0

        decrypted_text = "".join([chr(pp) for pp in li])
        return decrypted_text


crypto = cryptography()
crypto.key = [17, 5, 14, 5, 1, 17, 24, 32, 12, 11, 11, 8, 7, 8, 5, 3, 18, 20, 25]

encrypt = crypto.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=")
decrypt = crypto.decrypt(encrypt)

print(f"encrypt: {encrypt}")
print(f"decrypt: {decrypt}")
