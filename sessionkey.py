# Derive the AES-256 session key from the master key of the user

from secrets import token_urlsafe
from hashlib import sha256

master = 'thisisthemasterkey123'

nonce = token_urlsafe(nbytes=32).encode('utf-8')

master_hash = sha256(master.encode('utf-8')).digest()

# Combine master_hash and nonce using bitwise OR
combined = int.from_bytes(master_hash, byteorder='little') << (32 * 8) | int.from_bytes(nonce, byteorder='big')

# Use to_bytes to convert the combined integer to bytes before hashing
session_key = sha256(combined.to_bytes((combined.bit_length() + 7) // 8, byteorder='big')).digest()

print(len(session_key))
print(int.from_bytes(session_key))