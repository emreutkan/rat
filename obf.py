# WSL
# sudo apt update
# sudo apt install python3-pip

import subprocess
import sys
import base64

obf_file_name = 'python.py'

def obfuscate_py():
    with open(input('file address: ').replace('\'','').replace('[','').replace(']',''),'rb') as f:
        encode = base64.b64encode(f.read())
    with open('enc.py','w') as f:
        f.write(f'import base64\nexec(base64.b64decode({encode}))')


if __name__ == '__main__':
    obfuscate_py()


# WINDOWS 
    # to create the exe
        # run | pip install pyinstaller
        # run | pyinstaller --onefile python.py    
