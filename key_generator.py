import rsa

def generate_keys():

    public_key, private_key = rsa.newkeys(512)

    open("public.pem", "wb").write(
        public_key.save_pkcs1()
    )

    open("private.pem", "wb").write(
        private_key.save_pkcs1()
    )

    print("Keys generated successfully")