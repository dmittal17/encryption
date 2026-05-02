def encrypt_file(input_file, key):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        encrypted_data = bytearray()
        for byte in data:
            encrypted_data.append(byte ^ ord(key))

        with open("encrypted_file.txt", 'wb') as f:
            f.write(encrypted_data)

        print("Encryption complete.")

    except FileNotFoundError:
        print("File not found!")


def decrypt_file(input_file, key):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        decrypted_data = bytearray()
        for byte in data:
            decrypted_data.append(byte ^ ord(key))

        with open("decrypted_file.txt", 'wb') as f:
            f.write(decrypted_data)

        print("Decryption complete.")

    except FileNotFoundError:
        print("File not found!")


# Main program
print("PRESS 1 for ENCRYPTION")
print("PRESS 2 for DECRYPTION")

choice = int(input("Enter your choice: "))

file_name = input("Enter file name: ")
key = input("Enter a character key: ")

if len(key) != 1:
    print("Key must be a single character!")
else:
    if choice == 1:
        encrypt_file(file_name, key)
    elif choice == 2:
        decrypt_file(file_name, key)
    else:
        print("Invalid choice!")