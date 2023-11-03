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

        enc = ""
        for pp in li:
            enc += chr(pp)

        return enc.encode().hex()

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

        enc = ""
        for pp in li:
            enc += chr(pp)

        return enc


crypto = cryptography()
crypto.key = [10, 5, 11, 8, 12, 7, 13, 2, 14, 5]

encrypt = crypto.encrypt("Secret Message")
decrypt = crypto.decrypt(encrypt)

print(f"encrypt: {encrypt}")
print(f"decrypt: {decrypt}")
