
# Self Decrypting Logic
import os
import color
file_path = ''

def get_file_address():
    global file_path
    file_path = input('file address: ').replace('\'', '').replace('[', '').replace(']', '')
    if input(f'{file_path} is the file address? (y/n): ').lower() == 'n':
        file_path = ''
        get_file_address()

def base64_esd():
    import base64
    with open(file_path, 'rb') as f:
        encode = base64.b64encode(f.read())
    with open(f'base64-{os.path.basename(file_path)}', 'w') as f:
        f.write(f'import base64\nexec(base64.b64decode({encode}))')
    print('enc.py created')


def random_key():
    import secrets
    with open(file_path, 'rb') as file:
        data = file.read()

    key = secrets.token_bytes(16)
    iv = secrets.token_bytes(16)  # 16 bytes for the IV
    output = bytearray(iv)

    for i, byte in enumerate(data):
        output.append(byte ^ key[i % len(key)] ^ iv[i % len(iv)])

    key_str = str(list(key))
    output_str = str(list(output))

    with open(f'encrypted_{os.path.basename(file_path)}', 'w') as self_decrypting_file:
        decryption_logic = f"""
key = {key_str}
encrypted_data = {output_str}
iv = bytes(encrypted_data[:16])
encrypted_data = bytes(encrypted_data[16:])
output = bytearray()
for i, byte in enumerate(encrypted_data):
    output.append(byte ^ key[i % len(key)] ^ iv[i % len(iv)])
exec(output.decode())
"""
        self_decrypting_file.write(decryption_logic)


if __name__ == '__main__':
    get_file_address()
    if not os.path.exists(file_path):
        print('Invalid file address')
        exit()
    selection = input(f'{color.white("1. base64")} \n{color.white("2. RandomKey")}')
    if selection == '1':
        base64_esd()
    elif selection == '2':
        random_key()
    else:
        print('Invalid Selection')


# After this in a Windows environment, you can use pyinstaller to create an exe file
    # pip install pyinstaller
    # pyinstaller --onefile python.py
# the exe will not be detected by antivirus software because of the encryption, exe decrypts itself once its executed,
# however browsers, windows defender and other antivirus software will detect the exe as a threat (not the content itself), thats why it will fla
