
## DNS Remote Command Executor
A simple DNS-based remote command execution (RCE) tool that allows a client to send commands to a server using DNS queries. The tool encrypts the commands, sends them to the server, and then decrypts the server's response. This tool is built with Python and uses DNS for communication between the client and the server.
Features
Remote Command Execution (RCE): Send commands to the server through DNS queries.
AES Encryption: Commands are encrypted before being sent and decrypted upon receiving the response, ensuring secure communication.
Simple Setup: Easy to configure and use with a few command-line arguments.
About and Help Options: Built-in -help and -about options for user assistance.
## Features

- Remote Command Execution (RCE): Send commands to the server through DNS queries.
- AES Encryption: Commands are encrypted before being sent and decrypted upon receiving the response, ensuring secure communication.
- Simple Setup: Easy to configure and use with a few command-line arguments.
- About and Help Options: Built-in -help and -about options for user assistance.


## Screenshots

![App Screenshot](https://github.com/mrmtwoj/DNSrce/blob/754b0ff6f3782c82ddbb3be8741e5e90d5308d41/Screenshot%202025-02-03%20.png)


## Requirements

- Python 3.x
- cryptography library (for AES encryption/decryption)


## Installation

- Before running the tool, you need to install the required dependencies. You can install them using pip:



## Deployment

To deploy this project run

```bash
pip install cryptography
```


## Used By

Basic Command
To send a command to the server, use the following syntax:
```bash
python cli.py -ip <server_ip> -port <server_port> -rce "<command>"
```
- ip (optional): The IP address of the server (default is 192.168.20.147).
- port (optional): The port of the server (default is 53).
- rce (required): The command you want to execute on the server.


## How It Works

### Client:

+ The client sends a DNS query to the server with the command (e.g., ls) encrypted using AES encryption.
+ The command is transmitted via a UDP socket.
+ After sending the command, the client waits for the server's response, which is decrypted upon receipt.

### Server:

+ The server listens for incoming DNS queries, decrypts the command, executes it, and then sends the result back to the client.
+ The response is also encrypted before being sent back to the client.

## About 
+ Mr.mtwoj@gmail.com
+ acyber.ir
