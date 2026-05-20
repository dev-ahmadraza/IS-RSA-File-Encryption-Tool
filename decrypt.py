import rsa

def decrypt_file():

    private_key = rsa.PrivateKey.load_pkcs1(
        open("private.pem", "rb").read()
    )

    encrypted_message = open(
        "encrypted.txt",
        "rb"
    ).read()

    decrypted_message = rsa.decrypt(
        encrypted_message,
        private_key
    )

    open("decrypted.txt", "wb").write(
        decrypted_message
    )

    print("File decrypted successfully")