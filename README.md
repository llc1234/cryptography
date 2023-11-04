<h1> Simple Cryptography Class </h1>

This Python class implements a basic encryption and decryption algorithm. It allows for the encryption and decryption of strings using a simple technique based on manipulating hexadecimal values and a provided 'key'.



<h3>Usage</h3>
The class cryptography contains the following methods:

__init__(self)
Initializes the cryptography object with an empty key.

encrypt(self, string)
Takes a string as input and encodes it using a simple algorithm.
Converts the string to its hexadecimal representation and manipulates it using the provided key.
Returns the encrypted string as a hexadecimal-encoded string.

decrypt(self, string)
Takes an encrypted string (in hexadecimal format) as input.
Reverses the encryption process using the key to decode the string back to its original format.
Returns the decrypted string.


<h3>Important Notes</h3>
The key list used plays a crucial role in both encryption and decryption. Changing the key will significantly impact the encryption and decryption processes.
This implementation serves as a simple demonstration and is not recommended for secure encryption purposes due to its straightforward algorithm.
Please exercise caution when using this code for sensitive information. This code might not provide strong security against sophisticated attacks.
