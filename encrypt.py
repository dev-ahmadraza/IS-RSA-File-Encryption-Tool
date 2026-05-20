import rsa

def encrypt_file():

    public_key = rsa.PublicKey.load_pkcs1(
        open("public.pem", "rb").read()
    )

    message = open("sample.txt", "rb").read()

    encrypted_message = rsa.encrypt(
        message,
        public_key
    )

    open("encrypted.txt", "wb").write(
        encrypted_message
    )

    print("File encrypted successfully")