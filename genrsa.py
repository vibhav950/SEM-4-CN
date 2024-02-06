from Crypto.PublicKey import RSA
from Crypto import Random

def keygen():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)  # generate pub and priv key

    pub_key = key.publickey()  # pub key export for exchange

    pub_file = input("Enter filename to export public key.\n"
                    "You can share this key over the internet.\n\n")
    priv_file = input("Enter filename to export private key.\n"
                    "[CAUTION] Keep this file safe and DO NOT share it with anyone.\n\n")

    # Use exportKey to get a string representation of the public key
    pub_key_str = pub_key.exportKey().decode('utf-8')

    with open(pub_file, "w") as f:
        f.write(pub_key_str)

    print(f"Public key has been saved to {pub_file}")

    # Use exportKey to get a string representation of the private key
    priv_key_str = key.exportKey().decode('utf-8')

    with open(priv_file, "w") as f:
        f.write(priv_key_str)

    print(f"Private key has been saved to {priv_file}")


def main():
    print("Generate a new RSA keypair if you do not have one already.\n"
          "Save the keys after generation so you don't have to generate them again.\n\n")
    
    if (input("Generate a new keypair? (y/n) ").lower() == 'y'):
        keygen()

if __name__ == '__main__':
    main()