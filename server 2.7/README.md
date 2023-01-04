# Here is my code for the 2.6 exercise
server 4.4
# Ex 4.4 - HTTP Server Shell
# Author: Ofek Primor

# TO DO: import modules
import socket
import re
import os

# TO DO: set constants
import sys

IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 10
DEFAULT_URL = '/index.html'
REDIRECTION_DICTIONARY = {'/index': '/index.html'}
CANNOT_ACCESS = ['/secret.html']
REGEX = r'GET [\/\\\w\d\.\?]+ (HTTP/1.1)(\\r)*'
FIXED_RESPONSE = 'HTTP/1.1 200 OK\nContent-Type: text/plain\nContent-Length: 2\n\nOK'
ROOT_DIR = sys.argv[1]

def get_file_data(filename):
    """ Get data from file """
    print(f"{filename = }")
    if filename in CANNOT_ACCESS:
        return "403 - Cannot Access File".encode(), 403
    if not os.path.isfile(filename):
        return "404 - No File in Path".encode(), 404
    file = open(filename, 'rb')
    data = file.read()
    file.close()
    return data, 200  # send the binary data of file and 200 status code


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if resource in REDIRECTION_DICTIONARY:
        resource = REDIRECTION_DICTIONARY[resource]  # redirect if needed
        # TO DO: send 302 redirection response

    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    if resource == '' or resource == '/':
        url = ROOT_DIR + DEFAULT_URL  # send '/index.html'
    else:
        url = ROOT_DIR + resource

    filetype = os.path.splitext(url)[1]  # get file type from file path
    data, code = get_file_data(url)  # get the data and the status code
    if resource in CANNOT_ACCESS:
        data, code = get_file_data(resource)   # if cannot access send another data

    http_header = "HTTP/1.1 200 OK\r\n"
    http_header += f"Content-Length: {len(data)}\r\n"
    if filetype == '.html' or code != 200:
        http_header += "Content-Type: text/html; charset=utf-8\r\n\r\n"  # generate proper html header
    elif filetype == '.jpg':
        http_header += "Content-Type: image/jpeg\r\n\r\n"  # generate proper jpg header
    elif filetype == '.js':
        http_header += 'Content-Type: text/javascript; charset=UTF-8\r\n\r\n'  # generate proper js header
    elif filetype == '.css':
        http_header += 'Content-Type: text/css\r\n\r\n'  # generate proper css header
    elif filetype == '.ico':
        http_header += 'Content-Type: text/plain; charset=UTF-8\r\n\r\n' # generate proper ico header
    # TO DO: handle all other headers

    # TO DO: read the data from the file
    print(f"{filetype = } {url = } {http_header = }")
    client_socket.send(http_header.encode())  # send headers
    client_socket.send(data)  # send data


def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    get_req = request.split('\n')[0]  # get the request
    print(get_req)
    if re.match(REGEX, get_req):
        return True, get_req.split(" ")[1].replace('\\', '/')  # if it's a correct http request - return the path
    else:
        return False, "Not GET Request"


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    # client_socket.send(FIXED_RESPONSE.encode())
    while True:
        # TO DO: insert code that receives client request
        # ...
        client_request = client_socket.recv(1024).decode()
        valid_http, resource = validate_http_request(client_request)  # get the request and if it's good
        if valid_http:
            print('Got a valid HTTP request')
            print(resource)
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')  # if not a good GET request then print error and close connection
            break
    print('Closing connection')
    client_socket.close()


def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()
