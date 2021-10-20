#!/usr/bin/env python3

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 7777))
    server.listen(1)

    conn, addr = server.accept()
    print(f'[+] Connected:{addr}')

def send_data(data):
    data = data.encode()
    conn.send(data)

def get_data():
    data = conn.recv(10240).decode()
    return data

def main():
    while True:
        command = str(input('>>>'))

        if command == '':
            continue

        send_data(command)
        print(get_data())


if __name__ == '__main__':
    main()
