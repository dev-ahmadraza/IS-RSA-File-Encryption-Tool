from key_generator import generate_keys
from encrypt import encrypt_file
from decrypt import decrypt_file

while True:

    print("\n===== RSA FILE ENCRYPTION TOOL =====")
    print("1. Generate Keys")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Generate Keys
    if choice == "1":
        generate_keys()

    # Encrypt File
    elif choice == "2":
        encrypt_file()

    # Decrypt File
    elif choice == "3":
        decrypt_file()

    # Exit
    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")