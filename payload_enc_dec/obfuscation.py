# Self Decrypting Logic
import os

def base64_esd(file_path, output_file_destination=None):
    import base64
    with open(file_path, 'rb') as f:
        encode = base64.b64encode(f.read())

    if output_file_destination:
        destination = f'{str(output_file_destination).replace('.py', '')}-base64.py'
    else:
        destination = f'base64_{os.path.basename(file_path)}'
    with open(destination, 'w') as f:
        f.write(f'import base64\nexec(base64.b64decode({encode}))')
    return destination


def random_key(file_path, output_file_destination=None):
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

    if output_file_destination:
        destination = f'{str(output_file_destination).replace('.py', '')}-encrypted.py'
    else:
        destination = f'encrypted_{os.path.basename(file_path)}'
    with open(destination, 'w') as self_decrypting_file:
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
        return destination

# After this in a Windows environment, you can use pyinstaller to create an exe file
# pip install pyinstaller
# pyinstaller --onefile python.py
# the exe will not be detected by antivirus software because of the encryption, exe decrypts itself once its executed,
# however browsers, windows defender and other antivirus software will detect the exe as a threat (not the content itself), thats why it will fla
